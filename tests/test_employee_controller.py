import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app.controllers.employee_controller import employee_bp

class TestEmployeeController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(employee_bp, url_prefix="/employees")
        self.client = self.app.test_client()

    @patch("app.services.employee_service.EmployeeService.add_employee")
    def test_add_employee(self, mock_add_employee):
        mock_add_employee.return_value = None
        
        response = self.client.post("/employees/", json={"name": "John Doe", "position": "Engineer"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Employee added successfully"})
        mock_add_employee.assert_called_once_with({"name": "John Doe", "position": "Engineer"})

    @patch("app.services.employee_service.EmployeeService.get_employees")
    def test_get_employees(self, mock_get_employees):
        # Return a list of dictionaries instead of MagicMock objects
        mock_get_employees.return_value = [
            {"id": 1, "name": "John Doe", "position": "Engineer"},
            {"id": 2, "name": "Jane Smith", "position": "Manager"}
        ]

        response = self.client.get("/employees/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            [
                {"id": 1, "name": "John Doe", "position": "Engineer"},
                {"id": 2, "name": "Jane Smith", "position": "Manager"}
            ]
        )
        mock_get_employees.assert_called_once()

    @patch("app.services.employee_service.EmployeeService.get_employee")
    def test_get_employee(self, mock_get_employee):
        # Mock return value as a dictionary
        mock_employee = {"id": 1, "name": "John Doe", "position": "Engineer"}
        mock_get_employee.return_value = mock_employee

        response = self.client.get("/employees/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_employee)
        mock_get_employee.assert_called_once_with(1)

    @patch("app.services.employee_service.EmployeeService.update_employee")
    def test_update_employee(self, mock_update_employee):
        mock_update_employee.return_value = None
        
        response = self.client.put("/employees/1", json={"position": "Senior Engineer"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Employee updated successfully"})
        mock_update_employee.assert_called_once_with(1, {"position": "Senior Engineer"})

    @patch("app.services.employee_service.EmployeeService.delete_employee")
    def test_delete_employee(self, mock_delete_employee):
        mock_delete_employee.return_value = None
        
        response = self.client.delete("/employees/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Employee deleted successfully"})
        mock_delete_employee.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()
