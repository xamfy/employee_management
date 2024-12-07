from sqlalchemy.exc import SQLAlchemyError
from app.exceptions import DatabaseError
from app.models.employee import db, Employee


class EmployeeRepository:
    @staticmethod
    def create_employee(employee):
        try:
            db.session.add(employee)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseError(str(e))

    @staticmethod
    def get_employee_by_id(employee_id):
        try:
            return Employee.query.get(employee_id)
        except SQLAlchemyError as e:
            raise DatabaseError(str(e))

    @staticmethod
    def get_all_employees():
        try:
            return Employee.query.all()
        except SQLAlchemyError as e:
            raise DatabaseError(str(e))

    @staticmethod
    def update_employee(employee):
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseError(str(e))

    @staticmethod
    def delete_employee(employee):
        try:
            db.session.delete(employee)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseError(str(e))
