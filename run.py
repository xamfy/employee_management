from flask import Flask, jsonify
from app.models.employee import db
from app.controllers.employee_controller import employee_bp
from app.config import Config
from app.exceptions import ValidationError, NotFoundError, DatabaseError

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize DB
db.init_app(app)

# Register routes
app.register_blueprint(employee_bp)

# Global error handlers
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.message}), 400

@app.errorhandler(NotFoundError)
def handle_not_found_error(error):
    return jsonify({"error": error.message}), 404

@app.errorhandler(DatabaseError)
def handle_database_error(error):
    return jsonify({"error": "A database error occurred. Please try again later."}), 500

@app.errorhandler(Exception)
def handle_generic_error(error):
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == "__main__":
    # Create tables and run app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
