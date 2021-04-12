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

In container, start the backend:

```bash
# Run main.py in ~/rmt-fastapi/app/app/
python main.py
```

Open the URL in the host browser

```bash
http://0.0.0.0:8080/docs
```

Then you can now test the RESTful API made by FastAPI.