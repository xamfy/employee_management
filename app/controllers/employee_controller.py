from flask import Blueprint, request, jsonify
from app.services.employee_service import EmployeeService

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/", methods=["POST"])
def add_employee():
    data = request.get_json()
    EmployeeService.add_employee(data)
    return jsonify({"message": "Employee added successfully"}), 201

@employee_bp.route("/", methods=["GET"])
def get_employees():
    employees = EmployeeService.get_employees()
    # Handle cases where employees are dictionaries or objects
    return jsonify([
        emp if isinstance(emp, dict) else emp.__dict__ for emp in employees
    ]), 200

@employee_bp.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = EmployeeService.get_employee(employee_id)
    # Check if the object is already a dictionary
    if isinstance(employee, dict):
        return jsonify(employee), 200
    # Otherwise, convert to a dictionary (for actual Employee objects)
    return jsonify(employee.__dict__), 200


@employee_bp.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.get_json()
    EmployeeService.update_employee(employee_id, data)
    return jsonify({"message": "Employee updated successfully"}), 200

@employee_bp.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    EmployeeService.delete_employee(employee_id)
    return jsonify({"message": "Employee deleted successfully"}), 200
