# Final Backend API

A complete Flask backend project combining authentication, CRUD operations, and database integration.

---

## Overview

This project combines multiple backend concepts into a single API including authentication, database storage, and full CRUD functionality.

---

## Features

- User registration
- User login
- Create items
- Get all items
- Get item by ID
- Update item
- Delete item
- SQLite database integration

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- database.db → SQLite database
- README.md → Project documentation

---

## Endpoints

### Authentication

POST /register  
POST /login  

### Items

GET /items  
GET /items/<id>  
POST /items  
PUT /items/<id>  
DELETE /items/<id>  

---

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- JSON

---

## Run the Project

```bash
pip install -r requirements.txt
python app.py

----------------------
Author

Alhanoof Alabdullah
