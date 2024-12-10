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
