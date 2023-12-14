import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='week0_tutorials',
            executable='daughter1',
            name='daughter1',
            output='screen',
        ),
             Node(
            package='week0_tutorials',
              executable='daughter2',
            name='daughter2',
            output='screen',
        ),
             Node(
            package='week0_tutorials',
            executable='daughter3',
            name='daughter3',
            output='screen',
             ),
                    Node(
            package='week0_tutorials',
            executable='daughter4',
            name='daughter4',
            output='screen',
             ),
             Node(
            package='week0_tutorials',
            executable='basestation',
            name='basestation',
            output='screen',
    
        ),

    ])
