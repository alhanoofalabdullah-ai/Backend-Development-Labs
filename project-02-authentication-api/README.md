# Authentication API Lab

A simple Flask backend project for basic user authentication.

---

## Overview

This project demonstrates how to build a simple authentication API using Flask for user registration and login.

---

## Features

- Register a new user
- Login with username and password
- Validate request data
- Return JSON responses

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Register a new user
```http
POST /register

Login user

POST /login

Technologies Used

Python
Flask
REST API
JSON

Run the Project
Install dependencies

pip install -r requirements.txt

Start the server

python app.py

Example JSON
Register request body

{
  "username": "alhanoof",
  "password": "123456"
}

Login request body

{
  "username": "alhanoof",
  "password": "123456"
}

----------------------
Author

Alhanoof Alabdullah
