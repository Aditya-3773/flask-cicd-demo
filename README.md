# 🚀 Flask CI/CD Demo

A simple **Task Manager REST API** built with **Flask** to demonstrate a complete **CI/CD pipeline** using **GitHub Actions**, **Docker**, and **AWS EC2**.

This project focuses on automating the deployment process. Every change pushed to the `main` branch will eventually be tested, containerized, and deployed automatically to an EC2 instance.

---

## 📌 Project Overview

Instead of manually deploying code every time changes are made, this project automates the entire deployment workflow.

The application provides a simple Task Manager API while demonstrating modern DevOps practices such as:

- Version Control with Git & GitHub
- Continuous Integration (CI)
- Continuous Deployment (CD)
- Containerization using Docker
- Deployment to AWS EC2

---

## 🛠️ Tech Stack

- Python 3.13
- Flask
- Git
- GitHub
- GitHub Actions
- Docker
- Docker Hub
- AWS EC2

---

## 📂 Project Structure

```
flask-cicd-demo/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── app.py
├── Dockerfile
├── requirements.txt
├── requests.http
├── README.md
└── .gitignore
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Check API status |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Mark a task as completed |
| DELETE | `/tasks/<id>` | Delete a task |

---

## ▶️ Running the Project

### Clone the repository

```bash
git clone https://github.com/Aditya-3773/flask-cicd-demo.git
```

Move into the project folder

```bash
cd flask-cicd-demo
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

The API will be available at

```
http://127.0.0.1:5000
```

---

## 🧪 Testing

The project includes a `requests.http` file that can be used with the VS Code REST Client extension to test all API endpoints.

---

## 🔄 CI/CD Pipeline

The deployment workflow will perform the following steps:

```
Developer Pushes Code
        │
        ▼
 GitHub Repository
        │
        ▼
 GitHub Actions
        │
        ├── Run Tests
        ├── Build Docker Image
        ├── Push Image to Docker Hub
        └── Deploy to AWS EC2
```

---

## 📈 Current Progress

- ✅ Flask REST API
- ✅ Git & GitHub
- ✅ Project Structure
- ✅ Dockerfile
- ⏳ Docker Image Build
- ⏳ Docker Hub Integration
- ⏳ GitHub Actions
- ⏳ AWS EC2 Deployment

---

## 🚀 Future Improvements

- Store tasks in a database (SQLite/PostgreSQL)
- Add automated unit tests
- Use Amazon ECR instead of Docker Hub
- Deploy to a private EC2 instance
- Implement Blue-Green deployment
- Add monitoring and logging

---

## 👨‍💻 Author

**Aditya Dimri**

GitHub: https://github.com/Aditya-3773
