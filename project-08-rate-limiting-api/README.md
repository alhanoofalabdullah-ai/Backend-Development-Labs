# Rate Limiting API Lab

A Flask backend project for limiting API request rates.

---

## Overview

This project demonstrates how to protect an API by applying rate limits to incoming requests.

---

## Features

- Limit repeated requests
- Protect endpoints from abuse
- Return clear error messages
- Use Flask-Limiter with Flask

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Home endpoint
GET /

### Limited endpoint
GET /limited

---

## Technologies Used

- Python
- Flask
- Flask-Limiter
- REST API
- JSON

---

## Run the Project

### Install dependencies
```bash
pip install -r requirements.txt

Start the server

python app.py

Example Requests
Home endpoint

GET http://127.0.0.1:5000/

Limited endpoint

GET http://127.0.0.1:5000/limited

# If the request limit is exceeded, the API will return a rate limit error.

------------------
Author

Alhanoof Alabdullah
