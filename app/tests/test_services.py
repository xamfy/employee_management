from app.services.employee_service import EmployeeService
from app.models.employee import Employee
import pytest

def test_add_employee(mocker):
    mock_create = mocker.patch("app.repositories.employee_repository.EmployeeRepository.create_employee")
    data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "department": "Engineering",
        "date_joined": "2024-01-01"
    }
    EmployeeService.add_employee(data)
    mock_create.assert_called_once()

def test_add_employee_invalid_email(mocker):
    data = {
        "name": "Jane Doe",
        "email": "invalid-email",
        "department": "HR",
        "date_joined": "2024-01-01"
    }
    with pytest.raises(ValueError, match="Invalid email format"):
        EmployeeService.add_employee(data)

def test_get_employee(mocker):
    mock_get = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_employee_by_id")
    mock_get.return_value = Employee(id=1, name="John", email="john@example.com", department="Engineering", date_joined="2024-01-01")
    employee = EmployeeService.get_employee(1)
    assert employee.name == "John"
    mock_get.assert_called_once_with(1)
