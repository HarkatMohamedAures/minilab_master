import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory



minilab_model_share_directory = get_package_share_directory('minilab_model')
param_file = minilab_model_share_directory + '/map/buvette.yaml'


def generate_launch_description():
	print(param_file)
	return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'node_prefix',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), '_'],
            description='The map server, sends map messages to rviz and other navigation packages'),
        launch_ros.actions.Node(
            package='nav2_map_server', executable='map_server', output='screen',
            name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'map_server',],
            parameters = [
            	{"yaml_filename": param_file} 
            ]),
    ])



