#!/usr/bin/env python

#import roslib
#roslib.load_manifest('minilab_teleop')
#import rospy
#roslib and rospy are no longer supported in ROS2, rclpy should be used instead

import rclpy
from rclpy.node import Node
 
from geometry_msgs.msg import Twist
#all builtin messages can be used inchanged in ROS2
import sys, select, termios, tty, subprocess


msg = """
Minilab Teleop
---------------------------
   a    z    e
   q    s    d
   w    x    c
1/2 : +- cmd vel 10%
4/5 : +- linear cmd vel 10%
7/8 : +- angular cmd vel 10%
s : stop
"""

moveBindings = {      
        'z':(1,0),
        'e':(1,-1),
        'q':(0,1),
        'd':(0,-1),
        'a':(1,1),
        'x':(-1,0),
        'c':(-1,1),
        'w':(-1,-1),
           }

speedBindings={
        '1':(1.1,1.1),
        '2':(.9,.9),
        '4':(1.1,1),
        '5':(.9,1),
        '7':(1,1.1),
        '8':(1,.9),
          }

def getKey(old_settings):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return key

def saveTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

def main(args = None):
		
    speed = .2
    turn = 1
    subprocess.run('tty')
    settings = saveTerminalSettings()
    
    
    #print("Checking input...")
    #input()
    
    #rospy.init_node('keyboard_teleop_ZQSD')
    rclpy.init()
    #super().__init__('keyboard_teleop_ZQSD')
    node = Node('keyboard_teleop_ZQSD')
    #pub = rospy.Publisher('cmd_vel', Twist)
    pub = node.create_publisher(Twist, 'cmd_vel', 10)

    x = 0.0
    th = 0.0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0.0
    target_turn = 0.0
    control_speed = 0.0
    control_turn = 0.0
    print(f'{sys.stdin.isatty()}')  
    #settings = termios.tcgetattr(sys.stdin)
    try:
        print(msg)
        
        print(vels(speed,turn))
        while(1):
        	
            key = getKey(settings)
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                count = 0

                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            elif key == ' ' or key == 's' :
                x = 0.0
                th = 0.0
                control_speed = 0.0
                control_turn = 0.0
            else:
                count = count + 1
                if count > 4:
                    x = 0.0
                    th = 0.0
                if (key == '\x03'):
                    break

            target_speed = speed * x
            target_turn = turn * th

            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 0.02 )
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 0.02 )
            else:
                control_speed = target_speed

            if target_turn > control_turn:
                control_turn = min( target_turn, control_turn + 0.1 )
            elif target_turn < control_turn:
                control_turn = max( target_turn, control_turn - 0.1 )
            else:
                control_turn = target_turn

            twist = Twist()
            twist.linear.x = control_speed; twist.linear.y = 0.0; twist.linear.z = 0.0
            twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = float(control_turn)
            pub.publish(twist)

            #print("loop: {0}".format(count))
            #print("target: vx: {0}, wz: {1}".format(target_speed, target_turn))
            #print("publihsed: vx: {0}, wz: {1}".format(twist.linear.x, twist.angular.z))

    except:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    
if __name__=="__main__":	main()

