# Logging API Lab

A Flask backend project for logging API activity.

---

## Overview

This project demonstrates how to use logging in a Flask application to record API requests and important events.

---

## Features

- Log API activity
- Record successful requests
- Record invalid requests
- Save logs to a file
- Return JSON responses

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- app.log → Log output file
- README.md → Project documentation

---

## Endpoints

### Home endpoint
GET /

### Log message endpoint
POST /log

---

## Technologies Used

- Python
- Flask
- Logging
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
Log message request body

{
  "message": "Test log message"
}

---------------------
Author

Alhanoof Alabdullah
