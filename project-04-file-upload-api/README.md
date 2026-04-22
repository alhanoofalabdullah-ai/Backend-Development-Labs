# File Upload API Lab

A Flask backend project for uploading files.

---

## Overview

This project demonstrates how to build a simple file upload API using Flask.

---

## Features

- Upload a file
- Save uploaded files locally
- Validate file presence
- Return JSON responses

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- uploads/ → Uploaded files
- README.md → Project documentation

---

## Endpoints

### Upload a file
POST /upload

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

Test the API

Use Postman and send a POST request to:

POST http://127.0.0.1:5000/upload

Body type:

form-data

Key:

file

Author

Alhanoof Alabdullah
