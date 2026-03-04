from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Start the standard keyboard teleop node
    keyboard_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='keyboard_teleop',
        output='screen',
        prefix='gnome-terminal --', # Opens a new terminal window to capture your keystrokes, changed xterm to gnome-terminal for better compatibility
        remappings=[('/cmd_vel', '/cmd_vel')] # Ensures it publishes to the standard Twist topic
    )

    return LaunchDescription([
        keyboard_node
    ])