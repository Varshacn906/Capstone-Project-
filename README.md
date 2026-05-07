# Capstone Project – Cloud-Based Feedback Management System

## Project Overview

This project is a full-stack cloud-based feedback management system developed using frontend, backend, database, and containerization technologies.

The system allows users to submit feedback through a web interface. The feedback is processed by the backend API, stored in a PostgreSQL database, and displayed dynamically on the dashboard.

---

# Architecture Flow

User → Frontend → FastAPI Backend → PostgreSQL Database  
                             ↓  
                        ETL Processing  
                             ↓  
                     Dashboard Analytics

---

# Technologies Used

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI (Python)

## Database
- PostgreSQL

## Containerization
- Docker

## Infrastructure
- Terraform (Basic Setup)

---

# Features

- User-friendly feedback form
- Real-time data submission
- Backend API integration
- PostgreSQL database storage
- Dynamic dashboard table
- Containerized application using Docker
- Modular frontend structure using separate HTML, CSS, and JavaScript files

---

# How the Project Works

## Step 1 – User Interaction
The user opens the frontend application in the browser and enters:
- Name
- Feedback

When the user clicks the Submit button, JavaScript sends the data to the FastAPI backend using API requests.

---

## Step 2 – Backend Processing
The FastAPI backend receives the user data through REST APIs.

The backend:
- Validates the request
- Connects to PostgreSQL
- Inserts feedback data into the database

---

## Step 3 – Database Storage
PostgreSQL stores all submitted feedback records permanently in a table.

The database acts as the central storage layer for the application.

---

## Step 4 – Data Retrieval
The frontend sends another API request to fetch stored feedback data.

The backend retrieves records from PostgreSQL and returns them in JSON format.

---

## Step 5 – Dashboard Display
Using JavaScript, the frontend dynamically updates the HTML table and displays all stored feedback records to the user.

---

# API Endpoints

## Add Feedback
POST:
http://127.0.0.1:8000/add

## Get Feedback
GET:
http://127.0.0.1:8000/feedback

---

# Project Structure

Capstone-Project/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Dockerfile
├── requirements.txt
└── README.md

---

# How to Run the Project

## Backend

Run the following command:

uvicorn backend.main:app --reload

Backend runs on:
http://127.0.0.1:8000

---

## Frontend

Open:
frontend/index.html

in the browser.

---

# Future Enhancements

- User authentication
- Cloud deployment on AWS/Azure
- CI/CD pipeline integration
- Advanced analytics dashboard
- Monitoring and logging
- Docker Compose support

---

# Conclusion

This project demonstrates the implementation of a cloud-based full-stack application using modern development technologies including FastAPI, PostgreSQL, Docker, and frontend web technologies.

The project successfully integrates frontend, backend, database, ETL workflow, and containerization into a complete working system.
