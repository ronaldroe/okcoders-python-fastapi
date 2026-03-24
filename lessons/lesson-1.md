# FastAPI Microservice Lesson One

## Contents

  1. [Decorators](#decorators)
    1. [Concept](#concept)
    2. [Use in our Microservice](#use-in-our-microservice)
  2. [Schemas](#schemas)
    1. [Concept](#concept-1)
    2. [Advantages and Uses](#advantages-and-uses)
  3. [Enums](#enums)
    1. [Concept](#concept-2)
    2. [Advantages and Uses](#advantages-and-uses-1)
  4. [Understanding the project structure](#understanding-the-project-structure)
    1. [Dockerfile](#Dockerfile)
    2. [docker-compose.yml](#docker-compose.yml)
    3. [requirements.txt](#requirements.txt)
    4. Directory Structure
  5. [`main.py`](#mainpy)
    1. [Purpose](#purpose)
    3. [FastAPI instance and middleware](#fastapi-instance-and-middleware)
    4. [Fallback Exception Handler](#fallback-exception-handler)
    5. [Creating the routers](#creating-the-routers)

## Decorators

### Concept

Decorators are a feature of some languages that allow arguments to the decorated function to be intercepted in order to apply some common functionality to it. 

A common use case for decorators is logging. Rather than having to have a block of code on each of your methods to do your logging, you can create a decorator that takes the arguments to the function and logs them in a standard way. [Here is an excellent article](https://medium.com/learning-the-computers/its-a-wrap-s-python-logging-decorators-improve-troubleshooting-a96f4ab728d1) with an example of a logging decorator and a more in-depth explanation on decorators in general.

### Use in our Microservice

This project will use decorators for exception handling and routing.

## Schemas

### Concept

A schema is a method of easily validating request and response data. This makes applications more stable and secure by ensuring all inputs are of the expected type, and fit any other criteria that is needed. 

### Advantages and Uses

The main advantages of using schemas for validation are:

  - Stability - The application is more stable when incorrect input types or other issues are caught early, and can fail safely. If the application had no validation, an incorrect type on an input could cause serious issues when the data is persisted.
  - Security - User input should *always* be validated and sanitized. Schemas handle much of the heavy lifting for you.

## Enums

### Concept

Enums, or enumerations are a feature of many languages that allow applications to easily restrict the value of a given variable or input to a defined list of accepted values.

A practical example we will use in the health check endpoint will be a `health_statuses` enum, which will have two statuses: `HEALTHY` and `UNHEALTHY`.

### Advantages and Uses

The main advantages of enums are:

  - Easily restrict the value to a given set of acceptable values
  - Keep it DRY. If you need to change any of the values, you only have to change them in one spot for the entire application to use it.

## Understanding the Project Structure

This project is structured using a service-repository pattern. This pattern creates layers with strictly defined functionality. We will cover this more in the second lesson.

### [Dockerfile](../Dockerfile)

The Dockerfile is used to create the image for our containerized microservice. This project uses Python version 3.12, because some of the libraries have not yet been updated for later versions (as of Jan 2026). The last line issues the command to call uvicorn. Uvicorn is a Python web server.

### [docker-compose.yml](../docker-compose.yml)

The Docker compose yaml file is used to start and stop the container. This project doesn't require very much in terms of Docker compose, as it's a fairly simple microservice, and has no outside dependencies. If you were to use a Postgres database, that would be another container along with more config options. For instance, when you call `docker compose up okcoders-python-fastapi`, you would most likely want to have the database software to start as well.

### [requirements.txt](../requirements.txt)

The requirements.txt in the project lists all of the packages we will be using for the project.

  - `fastapi` - FastAPI is a library for quickly building REST or GraphQL APIs in Python
  - `pydantic` - A schema and validation library
  - `pydantic-core` a `pydantic` dependancy
  - `sqlalchemy` an Object Relational Mapping library for interacting with databases
  - `uvicorn` A Python web server

### Directory Structure

## `main.py`

### Purpose

`main.py` is the entrypoint for the microservice. It is called in the last line of the [Dockerfile](#dockerfile) by passing `main:app` to `uvicorn`. 

`main.py` instantiates FastAPI, adds middleware, creates a fallback exception handler and the routes for the API. Each of these is discussed in more detail below. There is a lot more that can be done in `main.py`. I recommend reading through the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/first-steps/) for this.

### FastAPI instance and middleware

The first thing the `main.py` does is create an instance of FastAPI as `app`. `app` is the root of the functionality of our API. For our application, we're going to pass in four keyword arguments.

  1. `docs_url` is going to be the path to the OpenAPI (Swagger) documentation, where you can send requests to the endpoints and see the schemas for each.
  2. `openapi_url` is the json file used by OpenAPI. This can imported into some other tools.
  3. `title`
  4. `version`

Next, any middleware required for the project is registered. For this project, we will be using the CORS and gzip middleware. Middleware is registered using the `app.add_middleware` method. `app.add_middleware` takes one positional and 4 keyword arguments for our use case.

There are a lot of middleware options available. The [FastAPI docs](https://fastapi.tiangolo.com/reference/middleware/) list several built in middleware. This repo lists several third party middleware. You can also write your own custom middleware.

  1. First Argument (positional) is the middleware class.
  2. `allow_origins` is the origins we're going to allow for this project.
  3. `allow_credentials` setting this to `True` enables our bearer token authentication we'll add later
  4. `allow_methods` the request methods we want to allow requests to use. When you deploy the microservice, you should list out the methods that the API has endpoints for. Setting it to `*` during early development makes things a bit easier. If you don't want to have to worry about changing it later, you can use an environment variable for it.
  5. `allow_headers` the request headers we want to allow. Same as with `allow_methods`, you should set this to the actual headers in production, which would be only the ones used by the API. 

### Fallback Exception Handler

Next, a fallback exception handler is created. This purpose of the handler is to catch any exceptions that the code does not, helping to ensure the exception is properly logged for debugging purposes. The exception handler is registered using the `@app.exception_handler` decorator.

### Creating the routers

Finally, the router is created using `app.include_router`. This router is the API layer we'll be creating in this lesson. The three arguments are passed to the `app.include_router` method for our project.

  1. `router` is the router we imported from our API layer
  2. `prefix` is the path to the API's endpoints. The path for each route will be appended to this
  3. `tags` are optional, but are used in OpenAPI to make the UI more friendly
