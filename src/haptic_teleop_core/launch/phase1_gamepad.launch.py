from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Dynamically find the config file path on any OS
    config_filepath = os.path.join(
        get_package_share_directory('haptic_teleop_core'),
        'config',
        'gamepad_config.yaml'
    )

    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        parameters=[{'deadzone': 0.1}]
    )

    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy_node',
        parameters=[config_filepath], # Pointing to the YAML file
        remappings=[('/cmd_vel', '/cmd_vel')]
    )

    return LaunchDescription([
        joy_node,
        teleop_node
    ])