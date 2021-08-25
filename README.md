# minilab_master
####Descreption####

minilab simulator in ROS2.

####################################################################################

####Dependencies####

This simulator requires the following packages and tools:

  colcon:
  
    https://docs.ros.org/en/foxy/Tutorials/Colcon-Tutorial.html#install-colcon
  
  joint_state_publisher:
      
     https://index.ros.org/p/joint_state_publisher/
  
  Nav2:
    
    https://navigation.ros.org/build_instructions/index.html
  
  Gazebo: 
    
    http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install
  
  gazebo_ros_pkgs: 
    
    http://gazebosim.org/tutorials?tut=ros2_installing

####################################################################################

####installation####

After downloading the simulator's packages, put them in the src folder of your ros2 workspace directory. You can create one by typing the following command:

  mkdir -p ros2_ws/src

Before starting the compilation, the urdf file minilab_equiped should be modified; each mesh tag must receive the full path to the mesh files in the minilab_model package*.

Next, you should build and compile the packages using colcon at the root of the workspace:

    cd ros2_ws
    colcon build
  
Now, you can run any example in the minilab_demo_packages launch folder using ros2 launch**.

Notice:

*Check the problems section

**Not all examples are functional and there are some stability issues while usine gazebo. check the problems and remaining work sections.

####################################################################################

####problems####

1/_ While using the robot description in minilab_model/urdf/minilab_equiped.urdf. Gazebo will not even start if the package:// relative urls are used in the mesh tags. To solve this problem, an absolute path had to be used instead.

2/_ Loading too many stl files in minilab_model/urdf/minilab_equiped.urdf will sometimes cause Gazebo to crash. A remedey to this is to delete the build  and install directories and then rebuild the packages from the root of the workspace:

    rm -r build install
    colcon build


   Note:
      This problem will be triggered only if more than 2 stl files are used regardless of their size. The error rised by gazebo is a segmentation fault, which seems       to indicate a memory allocation problem. This bug was not present in ROS1 and maybe is due to the gazebo_ros_pkgs package.
    
3/_ Due to the changing of the launch structure in ROS2, nodes no longer have access to the input of a terminal. This will rise a Termios error if the minilab_teleop keyboard nodes are used in a launch file. A workaround to this problem was to write a small shell script that runs the minilab_teleop nodes alone. This script is launched as an executable in the launch file of the package that required minilab_teleop nodes.
  
4/_ The navigation, slam and the laser examples in the simulator are still not fully functional. This is due, in part at least, to a problem in the laser scan messages. It could be that the description in the urdf file is not suitable for these packages and it should be changed, this is still a work in progress.  
