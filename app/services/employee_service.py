from app.repositories.employee_repository import EmployeeRepository
from app.models.employee import Employee
from app.exceptions import ValidationError, NotFoundError
from datetime import datetime
import re

class EmployeeService:
    @staticmethod
    def validate_employee_data(data):
        required_fields = {"name", "email", "department", "date_joined"}
        if not required_fields.issubset(data.keys()):
            missing = ", ".join(required_fields - data.keys())
            raise ValidationError(f"Missing required fields: {missing}")

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, data["email"]):
            raise ValidationError("Invalid email format.")

        try:
            datetime.strptime(data["date_joined"], "%Y-%m-%d")
        except ValueError:
            raise ValidationError("Invalid date format. Use YYYY-MM-DD.")

    @staticmethod
    def add_employee(data):
        EmployeeService.validate_employee_data(data)
        employee = Employee(**data)
        EmployeeRepository.create_employee(employee)

    @staticmethod
    def get_employee(employee_id):
        employee = EmployeeRepository.get_employee_by_id(employee_id)
        if not employee:
            raise NotFoundError(f"Employee with ID {employee_id} not found.")
        return employee

    @staticmethod
    def get_employees():
        return EmployeeRepository.get_all_employees()

    @staticmethod
    def update_employee(employee_id, data):
        employee = EmployeeRepository.get_employee_by_id(employee_id)
        if not employee:
            raise NotFoundError(f"Employee with ID {employee_id} not found.")
        EmployeeService.validate_employee_data(data)
        for key, value in data.items():
            setattr(employee, key, value)
        EmployeeRepository.update_employee(employee)

    @staticmethod
    def delete_employee(employee_id):
        employee = EmployeeRepository.get_employee_by_id(employee_id)
        if not employee:
            raise NotFoundError(f"Employee with ID {employee_id} not found.")
        EmployeeRepository.delete_employee(employee)
