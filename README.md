# minilab_master
####Descreption####

minilab simulator in ROS2.

####################################################################################
####Dependencies####
This simulator requires the following packages and tools:

  colcon https://docs.ros.org/en/foxy/Tutorials/Colcon-Tutorial.html#install-colcon
  
  joint_state_publisher https://index.ros.org/p/joint_state_publisher/
  
  Nav2 https://navigation.ros.org/build_instructions/index.html
  
  Gazebo http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install
  
  gazebo_ros_pkgs http://gazebosim.org/tutorials?tut=ros2_installing

####################################################################################
####installation####
After downloading the simulator's packages, put them in the src folder of your ros2 workspace directory. You can create one by typing the following command:

  mkdir -p ros2_ws/src
  
Next, you should build and compile the packages using colcon at the root of the workspace:

  cd ros2_ws
  colcon build
  
Now, you can run any example in the minilab_demo_packages launch folder using ros2 launch*.

Notice:
*Not all examples are functional and there are some stability issues while usine gazebo. check problems and remaining work sections.

####################################################################################


  
