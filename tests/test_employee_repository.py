import pytest
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.exceptions import DatabaseError
from sqlalchemy.exc import SQLAlchemyError
from run import app  # Import the app from run.py directly


@pytest.fixture
def mock_employee():
    return Employee(name="John Doe", email="john.doe@example.com", department="Engineering", date_joined="2024-01-01")


def test_create_employee_success(mocker, mock_employee):
    mock_add = mocker.patch("app.models.employee.db.session.add")
    mock_commit = mocker.patch("app.models.employee.db.session.commit")

    with app.app_context():
        EmployeeRepository.create_employee(mock_employee)

    mock_add.assert_called_once_with(mock_employee)
    mock_commit.assert_called_once()


def test_create_employee_failure(mocker, mock_employee):
    mock_add = mocker.patch("app.models.employee.db.session.add")
    mock_commit = mocker.patch("app.models.employee.db.session.commit", side_effect=SQLAlchemyError("Error"))

    with app.app_context():
        with pytest.raises(DatabaseError, match="Error"):
            EmployeeRepository.create_employee(mock_employee)

    mock_add.assert_called_once_with(mock_employee)
    mock_commit.assert_called_once()


def test_update_employee_success(mocker, mock_employee):
    mock_commit = mocker.patch("app.models.employee.db.session.commit")

    with app.app_context():
        EmployeeRepository.update_employee(mock_employee)

    mock_commit.assert_called_once()


def test_update_employee_failure(mocker, mock_employee):
    mock_commit = mocker.patch("app.models.employee.db.session.commit", side_effect=SQLAlchemyError("Error"))

    with app.app_context():
        with pytest.raises(DatabaseError, match="Error"):
            EmployeeRepository.update_employee(mock_employee)

    mock_commit.assert_called_once()


def test_delete_employee_success(mocker, mock_employee):
    mock_delete = mocker.patch("app.models.employee.db.session.delete")
    mock_commit = mocker.patch("app.models.employee.db.session.commit")

    with app.app_context():
        EmployeeRepository.delete_employee(mock_employee)

    mock_delete.assert_called_once_with(mock_employee)
    mock_commit.assert_called_once()


def test_delete_employee_failure(mocker, mock_employee):
    mock_delete = mocker.patch("app.models.employee.db.session.delete")
    mock_commit = mocker.patch("app.models.employee.db.session.commit", side_effect=SQLAlchemyError("Error"))

    with app.app_context():
        with pytest.raises(DatabaseError, match="Error"):
            EmployeeRepository.delete_employee(mock_employee)

    mock_delete.assert_called_once_with(mock_employee)
    mock_commit.assert_called_once()
