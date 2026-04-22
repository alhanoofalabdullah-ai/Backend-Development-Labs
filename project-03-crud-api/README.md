# CRUD API Lab

A Flask backend project demonstrating full CRUD operations.

---

## Overview

This project demonstrates how to build a RESTful API that supports Create, Read, Update, and Delete operations using Flask.

---

## Features

- Create a new item
- Get all items
- Get item by ID
- Update item
- Delete item

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Get all items
GET /items

### Get item by ID
GET /items/<id>

### Create item
POST /items

### Update item
PUT /items/<id>

### Delete item
DELETE /items/<id>

---

## Technologies Used

- Python
- Flask
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
Create item

{
  "name": "Laptop",
  "price": 1000
}

----------------------
Author

Alhanoof Alabdullah
