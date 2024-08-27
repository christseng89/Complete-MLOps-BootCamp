# MLflow - Docker

// Folder => Docker-for-ML

docker run -it --rm busybox
    exit

docker run -it --rm busybox sh
    ls -l
    ls bin -l
    exit

docker run --rm busybox echo Hello Busybox
    Hello Busybox
docker run -it --rm busybox ls -l
    
    drwxr-xr-x    2 root     root         12288 May 18  2023 bin
    drwxr-xr-x    5 root     root           360 Aug 26 12:04 dev
    drwxr-xr-x    1 root     root          4096 Aug 26 12:04 etc
    drwxr-xr-x    2 nobody   nobody        4096 May 18  2023 home
    ...

### Running the Docker Container
https://hub.docker.com/u/manifoldailearning
docker run -d -P --name catgif manifoldailearning/catgif
docker ps | grep catgif
docker port catgif
http://localhost:32768/

docker stop catgif
docker run -d -p 8888:5000 --name catgif manifoldailearning/catgif
http://localhost:8888/

### Working with Dockerfile
cd Docker-for-ML\flask-app

pip install flask
python app.py
http://127.0.0.1:5000/

docker build -t catgifv2 .
docker run -d -p 8880:5000 --name catgif2 catgifv2
http://127.0.0.1:8880/
