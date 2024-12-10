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
    
    # Serialize SQLAlchemy model instances to dictionaries
    return jsonify([
        serialize_employee(emp) if isinstance(emp, object) else emp for emp in employees
    ]), 200


# Helper function to convert SQLAlchemy model instances to dictionaries
def serialize_employee(emp):
    return {
        "id": emp.id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "date_joined": emp.date_joined.isoformat()  # Format date as string
    }

@employee_bp.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = EmployeeService.get_employee(employee_id)
    
    # If employee is a dictionary, return it directly
    if isinstance(employee, dict):
        return jsonify(employee), 200
    
    # Otherwise, serialize the Employee object manually
    return jsonify(serialize_employee(employee)), 200


@employee_bp.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.get_json()
    EmployeeService.update_employee(employee_id, data)
    return jsonify({"message": "Employee updated successfully"}), 200

@employee_bp.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    EmployeeService.delete_employee(employee_id)
    return jsonify({"message": "Employee deleted successfully"}), 200
