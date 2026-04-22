# Search & Filter API Lab

A Flask backend project for searching and filtering data.

---

## Overview

This project demonstrates how to build an API that supports searching and filtering records using query parameters.

---

## Features

- Get all products
- Search by name
- Filter by category
- Combine search and filter
- Return JSON responses

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- README.md → Project documentation

---

## Endpoints

### Get products
GET /products

### Search and filter products
GET /products?name=laptop&category=electronics

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

Example Requests
Get all products

GET http://127.0.0.1:5000/products

Search by name

GET http://127.0.0.1:5000/products?name=laptop

Filter by category

GET http://127.0.0.1:5000/products?category=electronics

Search and filter

GET http://127.0.0.1:5000/products?name=phone&category=electronics

-------------------
Author

Alhanoof Alabdullah
