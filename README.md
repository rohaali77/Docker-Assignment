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

## Working
### Logs
![image](https://github.com/user-attachments/assets/88db95ff-6e80-45d9-8c6c-2fbd7b48604d)
### Recipe Generator
![image](https://github.com/user-attachments/assets/8d6fdb98-3edb-4321-ab28-80083fd7780f)
### Ingredient Analyzer
![image](https://github.com/user-attachments/assets/8bc06979-21ee-4f90-9fed-de846d00502a)

## Creative Feature
