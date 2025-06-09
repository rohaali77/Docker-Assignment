# Docker-Assignment
# Recipe Generator & Ingredient Analyzer (Microservices App with Docker)

## Application Description
This is a microservices-based application that helps users find recipes and analyze the healthiness of ingredients.  
The application is made of two services:
- **Recipe Generator Service**: Returns a random recipe and its ingredients.
- **Ingredient Analyzer Service**: Accepts a list of ingredients and analyzes whether they are healthy.

## Microservices Architecture
[User (Browser/Postman)]
       |
       | GET /recipe
       V
[Recipe Generator (Flask)] ----> Sends ingredients ----> [Ingredient Analyzer (Flask)]

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
