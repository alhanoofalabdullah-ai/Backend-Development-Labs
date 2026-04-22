# Database API Lab

A Flask backend project for storing and retrieving data using SQLite.

---

## Overview

This project demonstrates how to connect a Flask API to an SQLite database for basic data storage and retrieval.

---

## Features

- Create database records
- Get all records
- Get record by ID
- Delete records
- Use SQLite with Flask

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- database.db → SQLite database file
- README.md → Project documentation

---

## Endpoints

### Get all users
GET /users

### Get user by ID
GET /users/<id>

### Create user
POST /users

### Delete user
DELETE /users/<id>

---

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- JSON

---

## Run the Project

### Install dependencies
```bash
pip install -r requirements.txt

Start the server

python app.py

Example JSON
Create user request body

{
  "name": "Alhanoof",
  "role": "Backend Developer"
}

-------------------------
Author

Alhanoof Alabdullah

