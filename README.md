# ECS Flask Web App

This project is a simple Python Flask web application containerized with Docker and deployed to Amazon ECS.

## Features
- Python Flask backend serving HTML, CSS, and JavaScript
- Containerized using Docker
- Pushed to Amazon
- Deployed to Amazon ECS with Fargate
- Scalable using ECS Service with Application Load Balancer

## Project Structure
ecs-webapp/

│── app.py # Flask application

│── requirements.txt # Python dependencies

│── templates/ # HTML files

│── static/ # CSS and JS files

│── Dockerfile # Container build instructions

│── .gitignore # Ignore unnecessary files


## Local Setup
```bash
# Clone repository
git clone https://github.com/KajalSund/ecs-webapp.git
cd ecs-webapp

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```
Access at: http://127.0.0.1:8080

## Docker Build
```bash
docker build -t ecs-webapp .
docker run -p 8080:8080 ecs-webapp
```

## ECS Deployment
1. Push image to Amazon ECR

2. Create ECS Task Definition

3. Create ECS Service with ALB

4. Access via ALB DNS URL

