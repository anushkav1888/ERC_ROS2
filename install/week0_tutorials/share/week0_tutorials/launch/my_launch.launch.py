import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='week0_tutorials',
            executable='node1',
            name='node1',
            output='screen',
        ),
             Node(
            package='week0_tutorials',
            executable='node2',
            name='node2',
            output='screen',
        ),
             Node(
            package='week0_tutorials',
            executable='node3',
            name='node3',
            output='screen',
        ),

    ])
