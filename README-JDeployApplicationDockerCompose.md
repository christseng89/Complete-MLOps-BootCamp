# Deploy Applications with Docker Compose

### Introduction to Docker Compose
- Compose is a Docker Tool that allows you to define and run multi-container Docker applications.
- It uses a YAML file to configure the application's services, networks, and volumes.
- Using the commands, the user can create and start all the services from the configuration file.

// Docker Compose Working 3 Steps
- Create a Dockerfile for the application.
- Define the services that make the application in a docker-compose.yml file.
- Run `docker-compose up` to start the application and run `docker-compose down` to stop the application.

// Multi-Container Applications Deployment with Docker Compose
- Docker Compose make use of project names to isolate the environment.
- The data for all the containers in a service is preserved in volumes.
- If a service has restarted but nothing has changed, Docker Compose will reuse the existing containers.
- We can use variables in the Docker Compose files to customize the service for different environments.

// Compose Commands
- docker-compose build - build or rebuild services from the Dockerfile.
- docker-compose run - run a one-off command on a service.
    docker-compose run app sh
    docker-compose run app python test.py

- docker-compose up
- docker-compose down
- docker-compose stop
- docker-compose restart
- docker-compose ps
- docker-compose logs

### Hands On - Docker Compose with Flask Application
docker-compose --version
    Docker Compose version v2.29.2-desktop.2

pip install redis

cd Deploy-Applications-Docker-Compose\flask-compose
docker-compose up -d

docker images | grep flask-compose-web
    flask-compose    latest     ab05298fbc9b   About a minute ago   317MB

http://localhost:8000/

// .:/code:
- The . on the left side refers to the current directory on your host machine (where the docker-compose.yml file is located).
- The /code on the right side refers to the directory inside the container where the host directory will be mounted.
- Purpose: Code Syncing for Development to mount the host directory . to the container directory /code. This allows you to edit files and see the changes without needing to rebuild the Docker image or restart the container.

// Edit app.py change the message in the app.py file.
http://localhost:8000/

docker-compose ps
docker-compose logs
docker-compose logs web
docker-compose run web sh
    ls -l
    exit
docker-compose run web env
docker-compose --help

docker-compose up --scale web=2 -d
    [+] Running 3/3
    ✔ Container flask-compose-redis-1  Running          0.0s 
    ✔ Container flask-compose-web-1    Running          0.0s  # 1st Instance
    ✔ Container flask-compose-web-2    Running          0.0s  # 2nd Instance
