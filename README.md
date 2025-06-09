# Docker-Assignment
# Recipe Generator & Ingredient Analyzer (Microservices App with Docker)

## Application Description
This is a microservices-based application that helps users find recipes and analyze the healthiness of ingredients.  
The application is made of two services:
- **Recipe Generator Service**: Returns a random recipe and its ingredients.
- **Ingredient Analyzer Service**: Accepts a list of ingredients and analyzes whether they are healthy.

## Microservices Architecture
[User (Browser/Postman)] ---> GET/recipe ---> [Recipe Generator (Flask)] ----> Sends ingredients ----> [Ingredient Analyzer (Flask)]

Both services are deployed in Docker containers and communicate over a custom Docker network.

## Tech Stack
|           Service           |  Technology  |
|-----------------------------|--------------|
| Recipe Generator API        | Python Flask |
| Ingredient Analyzer Service | Python Flask |

## Docker Usage
- Each service has its own **Dockerfile** and is containerized.
- A **custom Docker network** is created to allow services to communicate.
- A **shared volume is used to store logs** for monitoring purposes (creative feature).

## Docker Commands
- docker network create recipe-network
- docker build -t recipe-generator ./recipe-generator
- docker build -t ingredient-analyzer ./ingredient-analyzer
- docker run -d --name recipe-generator --network recipe-network -p 5000:5000 recipe-generator
- docker run -d --name ingredient-analyzer --network recipe-network -p 6000:6000 ingredient-analyzer
- docker logs recipe-generator
- docker logs ingredient-analyzer
- docker tag recipe-generator rooha/recipe-generator:v1
- docker tag ingredient-analyzer rooha/ingredient-analyzer:v1
- docker login
- docker push roha/recipe-generator:v1
- docker push roha/ingredient-analyzer:v1
- docker volume create recipe-logs
- docker run -d --name recipe-generator --network recipe-network -v recipe-logs:/logs -p 5000:5000 recipe-generator
- docker run -d --name ingredient-analyzer --network recipe-network -v recipe-logs:/logs -p 6000:6000 ingredient-analyzer
- docker run -it --rm -v recipe-logs:/logs alpine sh
- cat /logs/recipe.log

## Working
### Logs
![image](https://github.com/user-attachments/assets/88db95ff-6e80-45d9-8c6c-2fbd7b48604d)
### Recipe Generator
![image](https://github.com/user-attachments/assets/8d6fdb98-3edb-4321-ab28-80083fd7780f)
### Ingredient Analyzer
![image](https://github.com/user-attachments/assets/8bc06979-21ee-4f90-9fed-de846d00502a)

## Docker Hub Links
https://hub.docker.com/repository/docker/rooha/ingredient-analyzer/general
https://hub.docker.com/repository/docker/rooha/recipe-generator/general

## Creative Feature
To demonstrate Docker’s power in managing data persistence and inter-service coordination, we implemented a creative feature where both microservices — recipe-generator and ingredient-analyzer — log their activity into a shared volume. This allows centralized log access, monitoring, and debugging, even though both services are running in isolated containers.
### Screenshots
![image](https://github.com/user-attachments/assets/c80266ab-980a-43f0-912b-1ebd8faccaa4)
