# 🍵 Tea Authentication Website

A full-stack authentication and tea management web application built using **FastAPI**, **MongoDB**, **JWT Authentication**, and a simple **HTML, CSS, and JavaScript** frontend.

## 🚀 Features

- 👤 User Registration
- 🔐 User Login
- 🔑 JWT Authentication
- 🔒 Password Hashing
- 🍵 Tea Management (Add, View, Update, Delete)
- 📦 MongoDB Database Integration
- 🌐 RESTful API
- 💻 Responsive Frontend

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- MongoDB
- PyMongo
- JWT (python-jose)
- Passlib (bcrypt)

### Frontend
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```
Tea_Auth_Website/
│
├── database/
│   ├── __init__.py
│   ├── model.py
│   └── schemas.py
│
├── routes/
│   ├── auth.py
│   └── tea.py
│
├── utils/
│   ├── hashing.py
│   └── token.py
│
├── FRONTEND/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── style.css
│   └── script.js
│
├── configuration.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Tea-Auth-Website.git
```

### Navigate to the project

```bash
cd Tea-Auth-Website
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ MongoDB Setup

Start your local MongoDB server.

The application connects to:

```
mongodb://localhost:27017
```

Database Name:

```
auth_db
```

Collections:

- users
- teas

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📸 Screenshots

Add screenshots here after running the project.

- Login Page
- Register Page
- Dashboard
- Tea Management

---

## 📚 Learning Objectives

This project demonstrates:

- FastAPI fundamentals
- JWT Authentication
- Password Hashing
- MongoDB CRUD Operations
- REST API Development
- Frontend and Backend Integration

---

## 👩‍💻 Author

**Muskan Hassan**

GitHub: https://github.com/muskanhassan

LinkedIn: *(Add your LinkedIn profile link here)*

---

## ⭐ If you found this project helpful, don't forget to star the repository!