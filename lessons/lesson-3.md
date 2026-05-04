# FastAPI Microservice Lesson 3

## Contents

1. [Object Relational Mapping](#object-relational-mapping)
  1. [Concept](#concept)
  2. [Advantages](#advantages)
  3. [Disadvantages](#disadvantages)
2. [Models](#models)
    1. [Concept](#concept-1)
3. [User Service Layer](#user-service-layer)
  1. [Get and Create User Endpoints](#get-and-create-user-endpoints)
    1. [User Model](#user-model)
    2. [Repository Layer](#repository-layer)
4. [User Repository Layer](#user-repository-layer)
  1. [Building Queries](#building-queries)
    1. [From Models](#from-models)
    2. [With SQL Query](#with-sql-query)

### Object Relational Mapping

#### Concept

Object Relational Mapping (ORM) is the process of _mapping_ incompatible _objects_ to _relational models_. In other words, when your repository needs to request a user's data, it needs to translate the schema into a structure the relational database (in our case, SQLite) can understand. To facilitate this mapping, we use models. 

Models look a lot like schemas, in that they have field names, each field has a type and other metadata associated with it. Models are unique, however in that they are a representation of the schema's data in the actual database. Why does that matter? Because, as well see in a future lesson, a schema is a representation of a single set of data, but a model may retrieve that data from multiple tables via joins, subqueries or other methods. At the end, that data is mapped to a response schema that has no knowledge of where the individual values came from.

The example we will use in a future lesson is a sub-object containing the user's address information. We will update the response schema to include a billing and shipping address, but those addresses will come from an address table, not from the user's record on the user table.

#### Advantages

There are two primary advantages to using an ORM:
1. Security
2. Abstraction

__Security__ - One of the easiest to exploit vulnerabilities is what's called a SQL injection attack. In such an attack, you might add a portion of valid SQL to an input, which you could use to retrieve data you shouldn't have, overwrite or delete data or even create new records. To combat this, we created what are called parameterized queries. In a parameterized query, any user inputs are stored separately from the query itself, and represented by a `?` or SQL variable `:user_id` in the query. Then, the query is sent to the database, and is compiled without the data in it. The parameterized data is passed to the compiled query when it is executed. ORMs abstract much of this away, but still offer the ability to write parameterized SQL queries, as we'll see later. 

__Abstraction__ - ORMs abstract away much of the complexity of working directly with SQL, which not only makes development faster, but makes queries more stable, as the output is deterministic based on the input, so you always get the same result.

#### Disadvantages

There are two primary disadvantages to using an ORM:
1. Performance
2. Abstraction

__Performance__ - ORMs generally focus on making queries as stable and reliable as possible. Because of that, performance of the queries often suffers. The ORM may be executing a number of queries in succession, because it's likely to be more stable, but one query would have sufficed. This is where good working knowledge of the SQL language and the various implementations is very useful. 

__Abstraction__ - There is such a thing as _too_ much abstraction. It can make troubleshooting difficult, as errors or other issues may be hidden or lost behind multiple layers of abstraction. Furthermore, if the engineer using the ORM doesn't understand the underlying SQL, dumping may not be useful to help figure out any issues.

### Models

#### Concept

A model is a class that is a representation of the data in a database, and provides metadata about a table, its columns or fields, fields and their types, along with defaults and other meta. Models also allow for mapping and transform functionality, and form the primary structure used to communicate with a database via the ORM. 

In SQLAlchemy, models extend a `declarative_base` model, which we'll define in a database connection file, and import into our models. A user model might look like:

```python
class UserRecord(Base):
  __tablename__ = "users"
  __table_args__ = {"schema": "user"}
  id = Column("id", String, unique=True, default=UUID.uuidv4()) # SQLite doesn't support UUID as a type
  first_name = Column("first_name", String, nullable=False)
  last_name = Column("last_name", String, nullable=False)
  email = Column("email", String, nullable=False)
  phone = Column("phone", String) # Leave off nullable if optional
  is_active = Column("is_active", Boolean, default=True)
```

Models can also contain relationships within their class definitions (we'll see this in a future lesson), as well as calculated fields, and more. 

### User Service Layer

In the previous lesson, we created the basic service layer that returns dummy data to our API layer. This PR will complete the service layer, which will request data from the repository layer. At first, the repository layer will return dummy data, and in the next part of this lesson, we'll complete the repository layer for the Get and Create User endpoints.

`branch: lesson-3-1`

#### Get User Endpoint

##### User Model

The user model in the Models Concept section above is the model we'll use for our API:

```python
class UserRecord(Base):
  __tablename__ = "users"
  __table_args__ = {"schema": "user"}
  id = Column("id", String, unique=True, default=uuid.uuidv4()) # SQLite doesn't support UUID as a type
  first_name = Column("first_name", String, nullable=False)
  last_name = Column("last_name", String, nullable=False)
  email = Column("email", String, nullable=False)
  phone = Column("phone", String) # Leave off nullable if optional
  is_active = Column("is_active", Boolean, default=True)
```

##### Repository Layer

In the second PR for this lesson, we'll complete the repository layer. This will include setting up the database (SQLite), connecting to it from the repository and methods to get and create a user. 

Note that once these changes are made, everything's "real". In other words, you will only be able to get a user with its real id after it's been created.

### User Repository Layer

#### Building Queries

Queries can be passed to the ORM in two primary ways:

##### From Models

Once the user's request data is passed to the model, the model can be passed directly to the ORM to query the database

##### With SQL Query

SQLAlchemy can also accept SQL queries directly to run against the database. This can be useful for troubleshooting queries, or bypassing performance bottlenecks caused by how the ORM builds a given query. And sometimes a query may be complex enough that it's actually easier to pass directly rather than to build it out with the ORM functionally.

NOTE: When passing SQL queries to the ORM, it is vital that all user input is parameterized, validated and sanitized. Validation and sanitization will mostly be handled by the schemas and models in our case. Parameterization is on the developer to implement as a best practice. SQLAlchemy will absolutely allow you to pass the entire query directly. It's up to *you* to parameterize them.

`branch: lesson-4`
