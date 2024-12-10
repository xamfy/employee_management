# Employee Management System

This is a simple Employee Management System built with Python, Flask, and SQLAlchemy. It follows a layered architecture with controller, service, and repository layers. The system provides a RESTful API for managing employee records.

---

## Features

- CRUD operations on employees:
  - Add a new employee.
  - Retrieve all employees or a specific employee by ID.
  - Update an employee's details.
  - Delete an employee.
- Layered architecture for better code separation and maintainability.
- SQLAlchemy for database ORM with PostgreSQL or MySQL.
- Data validation and error handling across all layers.

---

## Requirements

- Python 3.8+
- Flask
- SQLAlchemy
- PostgreSQL or MySQL

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/employee-management.git
cd employee-management
```

### 2. Install Depedencies
Create a virtual environment and install the required packages:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure the environment variables
Create a `.env` file in the project root by renaming `.env.example` to `.env`. Replace the value of `DATABASE_URL` in the file with the DB URL of your postgres database. You can keep the same values for other environment variables.

### 4. Run the application server
Start the Flask server:
```bash
python run.py
```

The API will be available at http://127.0.0.1:5000.


## Testing
Run unit tests for the application:
```bash
pytest
```

## Running via Docker Compose
Run the following command in the project root to build and start both the application and the PostgreSQL database:
```bash
docker-compose up --build
```

To stop all the containers:
```bash
docker-compose down
```


## API Endpoints

Please import the `employee_management_api.postman_collection.json` file present in the project in your postman client.

### POST `/employees`
**Description**: Add a new employee.

**Request**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "date_joined": "2024-12-01"
}
```

**Response**:
```json
{
  "message": "Employee added successfully"
}
```

---

### GET `/employees`
**Description**: Retrieve all employees.

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "date_joined": "2024-12-01"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "department": "HR",
    "date_joined": "2024-01-15"
  }
]
```

---

### GET `/employees/{id}`
**Description**: Retrieve a specific employee by ID.

**Response**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "department": "Engineering",
  "date_joined": "2024-12-01"
}
```

---

### PUT `/employees/{id}`
**Description**: Update an employee's information.

**Request**:
```json
{
    "date_joined": "2024-12-01",
    "department": "HR",
    "email": "john.doe@example.com",
    "id": 1,
    "name": "John Doe"
}
```

**Response**:
```json
{
  "message": "Employee updated successfully"
}
```

---

### DELETE `/employees/{id}`
**Description**: Remove an employee.

**Response**:
```json
{
  "message": "Employee deleted successfully"
}
```
