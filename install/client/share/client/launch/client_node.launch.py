
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    """ld = LaunchDescription()

    global_parameters = os.path.join(
        get_package_share_directory('client')
    )

    client_node_test = Node(
        package='client',
        node_executable='client_node.py',
        name='client_n'
	
    )

    ld.add_action(client_node_test)

    return ld"""

    return LaunchDescription([
        Node(
            package='client',
            node_executable='client_node.py',
            name='client_n'
        )
    ])
