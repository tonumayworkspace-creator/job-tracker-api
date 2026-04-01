# 🚀 Job Tracker API (Full-Stack | FastAPI + JavaScript)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-yellow)
![Status](https://img.shields.io/badge/Project-Production--Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📌 Overview

A **production-ready Job Application Tracking System** built using **FastAPI (backend)** and **HTML/CSS/JavaScript (frontend)**.

This application allows users to:

* Register & login securely 🔐
* Track job applications 📊
* Perform full CRUD operations ⚙️
* Filter jobs by status (Applied / Interview / Rejected) 🔍

---

## 🔥 Features

* 🔐 JWT Authentication (Login/Register)
* 🔒 Password hashing using bcrypt
* 👤 User-specific job management
* 📦 Full CRUD operations (Create, Read, Update, Delete)
* 🔍 Filter jobs by status
* 💻 Interactive dashboard UI
* 💾 Token persistence (localStorage)
* ⚡ REST API with FastAPI
* 🗃️ SQLite database (easily scalable)

---

## 🧱 Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla)

---


## 📁 Project Structure

```
job-tracker-api/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── main.py
├── job_tracker.db
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/job-tracker-api.git
cd job-tracker-api
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install fastapi uvicorn sqlalchemy python-dotenv passlib[bcrypt] python-jose email-validator
pip install bcrypt==4.0.1
```

---

### 4️⃣ Run Backend

```
uvicorn main:app --reload
```

👉 Open Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### 5️⃣ Run Frontend

* Open `frontend/index.html`
* OR use VS Code Live Server

---

## 🔐 Authentication Flow

1. Register user
2. Login → receive JWT token
3. Token stored in localStorage
4. All API requests include:

```
Authorization: Bearer <token>
```

---

## 📊 API Endpoints

### Auth

* POST `/register`
* POST `/login`

### Jobs

* POST `/jobs`
* GET `/jobs`
* PUT `/jobs/{id}`
* DELETE `/jobs/{id}`
* GET `/jobs/filter?status=Applied`

---

## 🧪 Example Workflow

1. Register → Login
2. Add job applications
3. View all jobs
4. Filter applied jobs
5. Update/Delete entries

---

## 🚀 Future Improvements

* PostgreSQL integration
* Docker deployment
* Role-based authentication
* Email notifications
* Pagination & search
* React frontend

---

## 🧠 Key Learnings

* Building scalable REST APIs with FastAPI
* Implementing JWT authentication
* Designing relational database models
* Full-stack integration (frontend + backend)
* Debugging real-world issues (CORS, auth, hashing)

---

## 📌 Resume Highlight

**Job Tracker API (Full-Stack Project)**

* Built a scalable backend system using FastAPI with JWT authentication and REST APIs
* Implemented full CRUD operations with user-specific access control
* Designed relational database models using SQLAlchemy
* Developed frontend dashboard using JavaScript with real-time API integration
* Added filtering, authentication, and secure password hashing

---

## 🤝 Connect

* LinkedIn: https://www.linkedin.com/in/tonumay/
* GitHub: https://github.com/tonumayworkspace-creator/job-tracker-api

---

⭐ If you found this useful, consider giving it a star!
