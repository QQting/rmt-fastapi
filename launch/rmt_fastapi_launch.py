from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, SetEnvironmentVariable

def generate_launch_description():
    ld = LaunchDescription()
    ld.add_action(SetEnvironmentVariable('LD_LIBRARY_PATH', '/root/rmt_fastapi_ws/src/rmt_fastapi/rmt_fastapi/app/app/api/api_v1/robots/RMT_core'))
    rmt_fastapi_process = ExecuteProcess(cmd=['python', '/root/rmt_fastapi_ws/src/rmt_fastapi/rmt_fastapi/app/app/main.py'])
    ld.add_action(rmt_fastapi_process)

    return ld
