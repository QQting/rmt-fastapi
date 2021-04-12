# rmt-fastapi
ROS Management Tool - FastAPI example

## Prerequisite

1. Docker: https://docs.docker.com/engine/install/ubuntu/

## Docker

Build image from dockerfile:

```bash
docker build -t="rmt-fastapi" . 
```

Start the container from the built image:

```bash
docker run -it -p 8080:8080 --network=host --rm rmt-fastapi
```

In container, start the backend with ROS 2 command:

```bash
ros2 launch rmt_fastapi rmt_fastapi_launch.py
```

Alternatively, you can directly run the python program to start the backend:

```bash
cd /root/rmt_fastapi_ws/src/rmt_fastapi/rmt_fastapi/app/app/
python main.py
```

Then, open the URL in the host browser

```bash
http://0.0.0.0:8080/docs
```

Now, you can test the RESTful API.