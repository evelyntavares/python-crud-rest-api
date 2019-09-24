CRUD REST API in Python
=======================

This is a sample REST API running on Python3.7 exploring CRUD operations, using Flask, Flask-JWT, Flask-RESTful, Flask-SQLAlchemy, flask_swagger_ui and Docker container.


Running the application
-----------------------

Requires Docker.

On the python-crud-rest-api/code directory, it is necessary to build the container image:
docker build -t python-crud-rest-api .

The image container has everything needed to run the application. Now, just run the command:
docker container run -p 5000:5000 python-crud-rest-api

JSON Structure
---------------------

    {
    "products": [
        {
            "sku": 1,
            "name": "Black bean - 1 KG",
            "available_quantity": 10,
            "warehouses": [
                {
                    "location": "SP",
                    "quantity": 10,
                    "type": "ECOMMERCE"
                }
            ]
        }
    ]
}

How to use it
----------------
All endpoints related to Products and Warehouses, except get methods, requires jwt authentication. There are two endpoints that needs to be called first, so the jwt authentication works properly:

 - /register-users: registers the username and password informed;
 - /auth: authenticates the username and password informed, returning a valid token as the response.

After getting a valid token, it is necessary to pass this token in the header of the request.

Endpoints
------------
Users:
/auth - Authenticates user
/api/register-users - Registers user

Products:
GET /api/products          - Finds all products
GET /api/products/{sku}    - Finds product by sku
PUT /api/products/{sku}    - Updates an existing product
POST /api/products/{sku}   - Adds a new product
DELETE /api/products/{sku} - Deletes a product

Warehouses:
GET /api/warehouses                - Finds all warehouses
GET /api/warehouses/{location}    - Finds warehouses by location
PUT /api/warehouses/{location}    - Updates an existing warehouse
POST /api/warehouses/{location}   - Adds a new warehouse
DELETE /api/warehouses/{location} - Deletes a warehouse

There is a swagger documentation with more details on:
http://localhost:5000/swagger/.
