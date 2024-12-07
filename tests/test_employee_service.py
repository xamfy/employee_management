import pytest
from app.services.employee_service import EmployeeService
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.exceptions import ValidationError, NotFoundError

employee_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "Engineering",
    "date_joined": "2024-01-01"
}

updated_employee_data = {
    "name": "John Updated",
    "email": "john.updated@example.com",
    "department": "Engineering",
    "date_joined": "2024-02-01"
}

employee_instance = Employee(**employee_data)

def test_add_employee(mocker):
    mock_create = mocker.patch("app.repositories.employee_repository.EmployeeRepository.create_employee")
    
    EmployeeService.add_employee(employee_data)

    mock_create.assert_called_once()
    actual_employee = mock_create.call_args[0][0]
    
    assert actual_employee.name == employee_data["name"]
    assert actual_employee.email == employee_data["email"]
    assert actual_employee.department == employee_data["department"]
    assert actual_employee.date_joined == employee_data["date_joined"]

def test_add_employee_missing_fields(mocker):
    invalid_data = {
        "name": "Jane Doe",
        "department": "HR",
        "date_joined": "2024-01-01"
    }
    with pytest.raises(ValidationError, match="Missing required fields: email"):
        EmployeeService.add_employee(invalid_data)

def test_add_employee_invalid_email(mocker):
    invalid_data = {
        "name": "Jane Doe",
        "email": "invalid-email",
        "department": "HR",
        "date_joined": "2024-01-01"
    }
    with pytest.raises(ValidationError, match="Invalid email format"):
        EmployeeService.add_employee(invalid_data)

def test_get_employee_success(mocker):
    mock_get = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_employee_by_id", return_value=employee_instance)
    result = EmployeeService.get_employee(1)
    assert result.name == "John Doe"
    mock_get.assert_called_once_with(1)

def test_get_employee_not_found(mocker):
    mock_get = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_employee_by_id", return_value=None)
    with pytest.raises(NotFoundError, match="Employee with ID 1 not found."):
        EmployeeService.get_employee(1)

def test_get_employees(mocker):
    mock_get_all = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_all_employees", return_value=[employee_instance])
    employees = EmployeeService.get_employees()
    assert len(employees) == 1
    assert employees[0].name == "John Doe"
    mock_get_all.assert_called_once()

def test_update_employee_success(mocker):
    mock_get = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_employee_by_id", return_value=employee_instance)
    mock_update = mocker.patch("app.repositories.employee_repository.EmployeeRepository.update_employee")
    EmployeeService.update_employee(1, updated_employee_data)
    assert employee_instance.name == "John Updated"
    assert employee_instance.email == "john.updated@example.com"
    mock_get.assert_called_once_with(1)
    mock_update.assert_called_once_with(employee_instance)

def test_update_employee_not_found(mocker):
    mock_get = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_employee_by_id", return_value=None)
    with pytest.raises(NotFoundError, match="Employee with ID 1 not found."):
        EmployeeService.update_employee(1, updated_employee_data)

def test_delete_employee_success(mocker):
    mock_get = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_employee_by_id", return_value=employee_instance)
    mock_delete = mocker.patch("app.repositories.employee_repository.EmployeeRepository.delete_employee")
    EmployeeService.delete_employee(1)
    mock_get.assert_called_once_with(1)
    mock_delete.assert_called_once_with(employee_instance)

def test_delete_employee_not_found(mocker):
    mock_get = mocker.patch("app.repositories.employee_repository.EmployeeRepository.get_employee_by_id", return_value=None)
    with pytest.raises(NotFoundError, match="Employee with ID 1 not found."):
        EmployeeService.delete_employee(1)
