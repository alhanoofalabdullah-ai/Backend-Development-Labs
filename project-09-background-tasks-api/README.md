# Background Tasks API Lab

A Flask backend project for handling background tasks.

---

## Overview

This project demonstrates how to run background tasks in a Flask application without blocking the main request.

---

## Features

- Run tasks in background
- Non-blocking API requests
- Simulate long-running operations
- Return immediate response

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Home endpoint
GET /

### Run background task
POST /task

---

## Technologies Used

- Python
- Flask
- Threading
- REST API
- JSON

---

## Run the Project

### Install dependencies
```bash
pip install -r requirements.txt

Start the server

python app.py

Example Request
Start background task

POST http://127.0.0.1:5000/task

--------------------
Author

Alhanoof Alabdullah
