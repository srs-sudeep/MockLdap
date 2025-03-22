# Mock LDAP Service

A mock LDAP service for development and testing purposes. This service simulates an LDAP server with pre-configured users having different roles (Faculty and Student).

## Features

- Mock LDAP authentication
- Pre-configured users with different roles
- RESTful API interface
- FastAPI-based implementation

## Pre-configured Users

### Faculty Members
1. John Doe
   - Username: john.doe
   - Password: faculty123
   - Department: Computer Science
   - Role: Faculty

2. Jane Smith
   - Username: jane.smith
   - Password: faculty456
   - Department: Mathematics
   - Role: Faculty

### Students
1. Alice Johnson
   - Username: alice.student
   - Password: student123
   - Department: Computer Science
   - Role: Student

2. Bob Wilson
   - Username: bob.student
   - Password: student456
   - Department: Mathematics
   - Role: Student

## Setup

### Local Development
1. Install Poetry if not already installed:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Run the service:
   ```bash
   poetry run uvicorn app.main:app --reload --port 8001
   ```

### Docker Deployment
1. Install Docker and Docker Compose on Ubuntu:
   ```bash
   # Install Docker
   sudo apt-get update
   sudo apt-get install docker.io

   # Install Docker Compose
   sudo apt-get install docker-compose
   ```

2. Build and run the container:
   ```bash
   # Build and start the service
   sudo docker-compose up -d

   # View logs
   sudo docker-compose logs -f
   ```

3. Stop the service:
   ```bash
   sudo docker-compose down
   ```

## API Endpoints

### Authentication
- **POST** `/auth`
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
  Response:
  ```json
  {
    "success": true,
    "user_data": {
      "uid": "string",
      "cn": "string",
      "mail": "string",
      "employee_type": "faculty|student",
      "department": "string",
      "title": "string"
    }
  }
  ```

### Health Check
- **GET** `/health`
  ```json
  {
    "status": "healthy"
  }
  ```

## Documentation

Once the service is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc 
