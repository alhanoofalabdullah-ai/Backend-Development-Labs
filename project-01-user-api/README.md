# User API Lab

A simple Flask backend project for basic user management.

---

## Overview

This project demonstrates how to build a simple REST API using Flask for creating, viewing, and deleting users.

---

## Features

- Get all users
- Add a new user
- Delete a user

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Get all users
```http
GET /users

Add a new user

POST /users

Delete a user

DELETE /users/<id>

Technologies Used

- Python
- Flask
- REST API
- JSON

Run the Project
Install dependencies

pip install -r requirements.txt

Start the server

python app.py

Example JSON
Add user request body

{
  "name": "Alhanoof",
  "role": "Developer"
}

--------------------
Author

Alhanoof Alabdullah
