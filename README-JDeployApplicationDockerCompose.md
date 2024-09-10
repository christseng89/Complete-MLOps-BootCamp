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
