# OK Coders Fast API Microservice RESTful API Course

## About the Course

In this course, you will learn the basics for creating a RESTful API User microservice with a health check, 9 endpoints and persistence.

Technologies we will use:
  - Docker
  - SQLite
  - FastAPI
  - Pydantic
  - SQLAlchemy
  - OpenAPI (Swagger)

We will also learn about:
  - Clean Architecture
    - Service-Repository Pattern
  - Iterative Development
  - Planning/Architecting a Microservice
    - Why a Microservice?
  - Functional vs Object Oriented Patterns
  - Enumeration
  - Request/Response Schemas
  - Database Planning and Modeling
  - Database Access via an Object Relational Mapping (ORM) library (SQLAlchemy)
  - Decorators

At the end of this course, you will have:
  - A working, RESTful API Microservice for handling Users within an application
  - Containerized via Docker
  - Persistence in a database
  - 11 Endpoints with OpenAPI docs
    - 1 Health check endpoint
    - 4 User CRUD endpoints
    - 6 Address CRUD endpoints

Required software:
  - Latest Docker with Docker Desktop
    - If you're using Windows, [please see this guide](https://docs.docker.com/desktop/setup/install/windows-install/), as there are more steps on that platform
  - [Postman](https://www.postman.com/downloads/)
    - Or if you prefer another, similar API client like [Insomnia](https://insomnia.rest/download), that is fine
  - Code Editor of choice

## Lessons

### Lesson 1 - Introduction, Scaffolding, Health Check, Decorators

In this lesson, we will go over the basic structure of the project, understanding the Dockerfile, docker-compose.yml, requirements.txt and main.py files. These files form the basic scaffolding of our project.

We will complete a health check and get the microservice running in Docker with a successful health check response. We will cover a basic understanding of decorators, what they're for and how they fit into our project.

### Lesson 2 - Basics of the Service-Repository Pattern, Iterative Development, Schemas

In this lesson, we'll create request/response schemas for the Get User endpoint, complete the API layer for the User API, with one endpoint (Get User).

We will go over the basics of the Service-Respository pattern and how to use it to organize a project. We will begin understanding iterative development, and use schemas to describe and validate requests and responses. This lesson will also touch on the functional and object oriented styles.

### Lesson 3 - Complete User API CRUD, Add Database Persistence

In this lesson, we will build out the service and repository layers for the User API and add persistence (via SQLite).

We will complete the User API CRUD endpoints. Data will persist in an in-memory SQLite database accessed by ORM.

### Lesson 4 - Address API, Database Relationships

In this lesson, we will design the relationship between addresses and users and create the necessary API endpoints for address CRUD.

This will include linking tables, creating relationships, indices, constraints, etc.,

### Lesson 5 - Complete Address API

In this lesson, we will complete the Address API by creating endpoints to allow addresses to be assigned and deleted from customers

We will implement our link table relationship between users and addresses in the user API, and complete the flow for our user microservice!
