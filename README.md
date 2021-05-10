# rmt-fastapi
ROS Management Tool - FastAPI example

## Prerequisite

1. Docker: https://docs.docker.com/engine/install/ubuntu/

## Docker

Build image from dockerfile:

```bash
wget https://raw.githubusercontent.com/QQting/rmt_fastapi/main/Dockerfile
docker build -t="rmt-fastapi" . 
```

Start the container from the built image:

```bash
docker run -it -p 8080:8080 --network=host --rm rmt-fastapi
```

Start the backend in the container:

```bash
cd /root/rmt_fastapi/backend
./start_backend.sh
```

Then, open the URL in the host browser

```bash
http://0.0.0.0:8080/docs
```

Now, you can test the RESTful API.
