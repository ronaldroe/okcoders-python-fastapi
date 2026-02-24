# FastAPI Microservice Lesson 2

## Contents

1. [Service-Repository Pattern](#service-repository-pattern)
   1. [Concept](#concept)
   2. [Advantages and Uses](#advantages-and-uses)
2. [Iterative Development](#iterative-development)
   1. [Concept](#concept-1)
   2. [Advantages and Uses](#advantages-and-uses-1)
3. [Functional and Object Oriented Styles](#functional-and-object-oriented-styles)
   1. [Functional](#functional)
      1. [Advantages and Disadvantages](#advantages-and-disadvantages)
   2. [Object Oriented](#object-oriented)
      1. [Advantages and Disadvantages](#advantages-and-disadvantages-1)
4. [User API Layer](#user-api-layer)
   1. [Setup](#setup)
   2. [Get User Endpoint](#get-user-endpoint)
      1. [Response Schema](#response-schema)
      2. [Service layer](#service-layer)
   3. [Create User Endpoint](#create-user-endpoint)
      1. [Request Schema](#request-schema)
      2. [Response Schema](#response-schema-1)
      3. [Service Layer](#service-layer-1)

## Service-Repository Pattern

The Service-Repository pattern is a common API pattern that creates layers with strictly defined roles to compartmentalize functionality. This compartmentalization helps keep functionality organized, which makes understanding the code easier and development in general faster. 

### Concept

Think of the Service-Repository pattern like a restaurant. 

 1. The host/hostess is the API layer. They determine where each diner (request) who enters should end up (routing)
 2. The server is the service layer. They're responsibility is to understand what you're requesting and get the information to the right person. They then collect the things that were requested and return them to the table (response). As a server would communicate with the kitchen, management, bar staff, bussers, etc., so does the service layer communicate with all of the other entities to gather, map and transform data related to the request
 3. The cooking line are your repository layer. The server passes the requested meals to the line, the line prepares it and hands it back to the server. The repository layer is for data access. Looking at our Get User endpoint, the service layer passes the user's `id` to the repository layer. The repository layer takes that ID, retrieves and returns the record.
    1. Note: In general, all data access should come from the repository layer. This includes databases, caches and REST/Other API calls. However, you will sometimes see REST and other API calls separated into their own layer. Whether this pattern is right for your project will depend on a number of factors. What's important to bear in mind is that each of these functionalities should at the very least be in their own class.

There can be any number of other layers the service layer might access, depending on how the project is organized. Any mapping or transforming of data or other business should be done in a business layer that the service calls, etc., We will not be creating other layers for this project.

### Advantages and Uses

  1. Decoupling technologies - If we decided to switch to a PostgreSQL database, it would only need changed in the repository layer (and in the models, to account for platform differences if needed). The same implies if we need to change a schema or a library that's been deprecated
  2. Maintainability - Functionality is organized into logical buckets. If data is coming out malformed, start in your mapper. If there's a database error, there's only one place to find the issue.
  3. Testability - You only need to create mocks for the repository layer in order to test all of the others
  4. DRY (Don't Repeat Yourself) - API layers can call multiple services for data, and services can call multiple repositories and so on without having to rewrite that code.

## Iterative Development

### Concept

Iterative development is a structured process for software development where work is broken down into small, functional pieces, and each new piece of work adds onto the previous. In an iterative approach to the Service-Repository, we'll build out the service by layers, using what I call the "Next Layer" method.

In this method, each pull request contains functional, testable software. You start with the API layer, and complete that layer. Any other layers it depends on (generally just the service layer) are created, but return dummy data. At this point, the API layer can be tested as if the endpoint were complete. In the next PR, complete the service layer and any layers it calls. The service layer should be fully formed, and the layers it calls should exist and return dummy data. And so on until the endpoint is fully functional and complete.

### Advantages and Uses

The advantages of iterative development is that it enables you to continuously test, both manual and automated, that the API does exactly what you expect. If a response comes out incorrect, it's easy to tell when that issue was introduced ("it worked 5 minutes ago!"). 

It allows anyone to pick up the work if needed. If you're building out an endpoint and have a family emergency, there's no long "knowledge transfer" sessions to do. You can simply pass it off and make sure the new engineer understands the overall requirements of the endpoint itself.

It increases developer velocity, reduces bugs, and a number of other advantages. If you haven't read Robert C. Martin's _The Clean Coder_, I highly recommend it. I believe it's essential reading for software engineers, and he goes into great depth on iterative processes and their importance and advantages. 

## Functional and Object Oriented Styles

### Functional - Concept

In functional programming, functionality is divided into modules with exported functions. Functions must be "pure". In other words, they cannot change application state or have any other side effects on mutable data. Data is passed to the function, it executes, and the returned result is a new data structure. 

For example:

```python
# This is INCORRECT, because it mutates `old_list`.
# The list you pass in will have `new_item` appended.
# Sometimes this is desired behavior, but is not allowed in
# functional programming
def add_to_list(new_item, old_list = []):
   return old_list.append(new_item)

# This is correct, because in Python, when you assign
# a list to a new variable, it makes a copy (unlike JS).
# The copy is returned with the new item appended
# The old list is unaffected
def add_to_list(new_item, old_list = []):
   new_list = old_list
   return new_list.append(new_item)
```

Data and the functions that operate on it are kept deliberately separate.

#### Advantages and Disadvantages

The advantages of functional programming are primarily predictability and concurrency. Functions that don't mutate the data they're passed are highly predictable. You can confidently assume (assuming your team is strict about adhering) that a function can take in parameters, and what you put back into the state is exactly what you expect. Further, because you're not operating directly on state, you don't have to worry about separate threads or processes mutating it in unpredictable ways.

The disadvantages are primarily memory usage and cognitive load. Because every time you pass data into a function it must return a new structure, you will often see things like the "correct" `add_to_list` function above, where data is copied and operated on. That naturally creates a lot more memory overhead. Readability is king, because code is read far more often than it is written. Functional software is naturally more difficult to troubleshoot, because the functionality, while it should be in modules with other functions that have related purposes is spread across many files, you will spend much more time jumping from file to file as you work. That becomes tedious and fatiguing over time, making you less effective.

### Object Oriented - Concept

In object oriented programming, related functionality is encapsulated into classes containing all of the properties (variables) and methods (functions). The classes are "instantiated", which creates an object that is used to access the properties and methods to operate on data. Methods can also be `static`, which means they can be called directly without an instance of the class.

Sometimes, certain aspects of functional programming may be used with object oriented software as well. Particularly pure functions. In this case, your methods would still not directly mutate data, but the state they do mutate is generally part of the class itself.

#### Advantages and Disadvantages

The advantages of object oriented programming are widely documented and many, but here are a few:

   - Encapsulation - The internals are hidden, meaning the rest of the software doesn't need to care about the details. Just instance the class and call the methods
   - Inheritance - Using parent/child classes allows similar structures to have differing underlying functionality. Keep it dry

Disadvantages:

   - Because the state is often not centrally handled, one change in a distant class can effect the outcome of another class. This can create bugs in mutable data if not handled carefully
   - It can be hard to define at times what functionality should be where. Because of that, a lot of OOP projects have either incredibly massive classes or the same "all over the place" problem functional has.

## User API Layer

### Setup

As with the health API layer, we'll create a router named after our API. This requires importing FastAPI and some other supporting packages. 

### Get User Endpoint

Because we're using the Service-Repository pattern, our first iteration for each endpoint will look similar to how the health endpoint does, but with subsequent layers stubbed out and returning dummy data. It will return an instance of `UserResponseSchema` encoded as JSON that contains some dummy information.

#### Response Schema

The `UserResponseSchema` will contain all of the basic non-address data for our users.

The response schema will have, at minimum, the following structure:

```JSON
{
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "is_active": true,
}
```

---

Note: while we are using UUIDs, when we add our SQLite database later, we will have to use the string type, as SQLite does not support UUIDs directly. In a production environment, you could convert the UUID to string on insert, and back again on retrieval. However, in production you wouldn't want to use a SQLite database. More robust SQL databases that you _would_ use in production, like PostgresSQL, do have UUID support, and you can use them directly.

---

Feel free to add any other information you think is important. Be sure to pick the appropriate type for each and add them to the example.

Take a moment to test your new endpoint. Ensure it returns the data you expect in the format you expect

`branch: lesson-2-1`

#### Service Layer

The second iteration for each endpoint is its service layer. The health endpoint has no need to communicate with any other layers, as it performs no logic. It gathers information from the environment and returns it. Our user endpoint, however will need to eventually access a database, and so will need to call our repository layer. This will be done from the service layer. 

You will need to create a repository layer which the service layer will call for user data from the data store the repository has access to. As we're working iteratively, this means we will create a repository layer that returns our dummy information. The service layer will then pack that data into a `JSONResponse` and return it to the API layer.

`branch: lesson-3`

### Create User Endpoint

As with the Get User endpoint, the first iteration for Create User is the API layer receiving the request and returning some dummy data. However for this endpoint, we'll have two schemas. One for the request, and one for the response. 

#### Request Schema

The `CreateUserRequestSchema` is very similar to the `UserResponseSchema`, minus the `id` field. 

One way to create this schema is to recreate the same one without the `id` field.

Another option is to create a `CreateUserRequestSchema` and have `UserResponseSchema` extend it and add the ID. Alternatively, you could have a `BaseUserRequestSchema`, and do something like `from schemas.requests.base import BaseUserRequestSchema as CreateUserRequestSchema` for your create endpoint. I will demonstrate this method, but how you implement for this project is up to you. There are advantages and disadvantages to each.

#### Response Schema

In the case of the Create User and Update User endpoint response schemas, we can use the same schema as the Get User endpoint: `UserResponseSchema`.

Once that schema is added to as the response model on the decorator, take a moment to test your Create User endpoint.

`branch: lesson-2-1`

#### Service Layer

As with the Get User endpoint's service layer, we will create a repository layer to return our dummy data, which is then returned to the api layer.

`branch: lesson-3`
