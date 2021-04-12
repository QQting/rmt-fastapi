from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, SetEnvironmentVariable

def generate_launch_description():
    ld = LaunchDescription()
    #ld.add_action(SetEnvironmentVariable('RMW_IMPLEMENTATION', 'rmw_cyclonedds_cpp'))
    rmt_fastapi_process = ExecuteProcess(cmd=['python', '/home/ros/rmt-fastapi/app/app/main.py'])
    ld.add_action(rmt_fastapi_process)

    return ld
