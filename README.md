# Address Book 

## Description

This is a rudimentary, REST-API based CRUD address book built using Django and DRF (Django Rest Framework). 
It uses SQLite as its database, and the SQLite file is also committed to the repository for easier access to 
pre-populated data.

## Getting Started

### Prerequisites

Install Python 3.7.3 and pip3 and run the following command to install other requirements

```pip3 install -r requirements.txt```

### Starting the server on local
Run the following command to start a Django WSGI server on your local on port 8000

```python manage.py runserver```

### Creating users to authenticate yourself
Every action requires you to authenticate yourself.
The SQLite database in the repository already has 2 users created with the following credentials

```username : admin password : admin```
```username : admin2 password : admin2```

You can use any of the above 2 users to login or create your own by running the following command

```python manage.py createsuperuser```


## Construct of the project structure
Note: All SQL queries are logged onto the console. If you want to log them into a file, you can 
change the handler in the logging settings in settings.py.
##### Apps
1. User - for storing a unique user
2. Address - for storing each unique address of a user

##### APIs
1. GET /users - gives list of users that you created
2. GET /users/<pk> - shows the particular user instance details
3. POST /users - creates a new user
4. PUT /users/<pk> - edits an existing user
5. DELETE /users/<pk> - deletes an existing user (only soft deletion)
6. GET /addresses - gives list of addresses that you created
7. GET /addresses/<pk> - shows the particular address instance details
8. POST /addresses - creates a new address
9. PUT /addresses/<pk> - edits an existing address
10. DELETE /addresses/<pk> - deletes an existing address (only soft deletion)

##### Sample screenshots of the APIs in your browser, along with SQL logs

![alt text](https://github.com/SidSamPaysense/address-book-crud/blob/master/staticfiles/user_instance.png?raw=true)

![alt text](https://github.com/SidSamPaysense/address-book-crud/blob/master/staticfiles/user_list.png?raw=true)

![alt text](https://github.com/SidSamPaysense/address-book-crud/blob/master/staticfiles/create_user.png?raw=true)

![alt text](https://github.com/SidSamPaysense/address-book-crud/blob/master/staticfiles/address_instance.png?raw=true)

![alt text](https://github.com/SidSamPaysense/address-book-crud/blob/master/staticfiles/address_list.png?raw=true)

![alt text](https://github.com/SidSamPaysense/address-book-crud/blob/master/staticfiles/create_address.png?raw=true)

![alt text](https://github.com/SidSamPaysense/address-book-crud/blob/master/staticfiles/sql_logs.png?raw=true)
