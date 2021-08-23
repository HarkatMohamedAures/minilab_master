import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory



minilab_model_share_directory = get_package_share_directory('minilab_model')
map_file = minilab_model_share_directory + '/map/buvette.yaml'

minilab_navigation_share_directory = get_package_share_directory('minilab_navigation')
param_file = minilab_navigation_share_directory + '/config/nav2_params.yaml'

def generate_launch_description():
	print(param_file)
	return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='nav2_map_server', executable='map_server', output='screen',
            name='map_server',
            parameters = [
            	{"yaml_filename": map_file} 
            ]),
		launch_ros.actions.Node(
            package='nav2_amcl', executable='amcl',
            name='amcl',
            parameters = [
            	{"yaml_filename": param_file} 
            ]),
    ])



