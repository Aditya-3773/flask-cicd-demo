#  Flask CI/CD Demo

A **Task Manager REST API** built with **Flask**, deployed through a fully automated **CI/CD pipeline** using **GitHub Actions**, **Docker**, **Docker Hub**, and **AWS EC2**.

Every push to `main` is automatically built, containerized, pushed to Docker Hub, and deployed to a live EC2 instance — no manual deployment steps.

---

##  Project Overview

Instead of manually deploying code every time changes are made, this project automates the entire deployment workflow end to end.

The application provides a simple Task Manager API while demonstrating modern DevOps practices:

- Version control with Git & GitHub
- Continuous Integration (CI) — build & test on every push
- Continuous Deployment (CD) — automatic deploy to EC2
- Containerization with Docker
- Image distribution via Docker Hub
- Deployment to AWS EC2

---

##  Tech Stack

- Python 3.13
- Flask
- Git & GitHub
- GitHub Actions
- Docker
- Docker Hub
- AWS EC2

---

##  Project Structure

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

##  API Endpoints

| Method | Endpoint      | Description               |
|--------|---------------|----------------------------|
| GET    | `/`           | Check API status           |
| GET    | `/tasks`      | Get all tasks              |
| POST   | `/tasks`      | Create a new task          |
| PUT    | `/tasks/<id>` | Mark a task as completed   |
| DELETE | `/tasks/<id>` | Delete a task              |

---

##  Running the Project Locally

Clone the repository:
```bash
git clone https://github.com/Aditya-3773/flask-cicd-demo.git
cd flask-cicd-demo
```

Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the app:
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`

---

##  Running with Docker

```bash
docker build -t flask-cicd-demo .
docker run -p 5000:5000 flask-cicd-demo
```

---

##  Testing

The project includes a `requests.http` file that can be used with the VS Code REST Client extension to test all API endpoints locally.

---

##  CI/CD Pipeline

Every push to `main` triggers the following automated workflow:

```
Developer Pushes Code
        │
        ▼
 GitHub Repository
        │
        ▼
 GitHub Actions
        │
        ├── Build Docker Image
        ├── Push Image to Docker Hub
        └── Deploy to AWS EC2 (pull latest image + restart container)
```

**Pipeline stages, in detail:**
1. **Checkout** — pulls the latest code from `main`
2. **Build** — builds the Docker image from the `Dockerfile`
3. **Push** — tags and pushes the image to Docker Hub
4. **Deploy** — SSHes into the EC2 instance, pulls the new image, stops the old container, and starts the new one

Credentials (Docker Hub token, EC2 SSH key) are stored securely as **GitHub Actions Secrets** — never hardcoded in the repo.

You can watch a live pipeline run under the [Actions tab](https://github.com/Aditya-3773/flask-cicd-demo/actions).

---

##  Project Status

-  Flask REST API - done
-  Git & GitHub - done
-  Project structure - done
-  Dockerfile - done
-  Docker image build - done
-  Docker Hub integration - done
-  GitHub Actions workflow - done
-  Automated deployment to AWS EC2 - done

**The pipeline is fully functional** — every push to `main` results in an automatic, zero-touch deployment.

---

## 🚀 Future Improvements

- Store tasks in a persistent database (SQLite/PostgreSQL) instead of in-memory storage
- Add automated unit tests as a pipeline stage before build/deploy
- Use Amazon ECR instead of Docker Hub for image storage
- Deploy to a private subnet EC2 instance with SSM tunneling
- Implement blue/green or rolling deployments for zero downtime
- Add monitoring and centralized logging (CloudWatch)

---

## 👨‍💻 Author

**Aditya Dimri**
GitHub: [Aditya-3773](https://github.com/Aditya-3773)
