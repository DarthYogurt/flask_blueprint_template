# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_tech.controllers import mod_tech as tech_module
from app.mod_category.controllers import mod_category as category_module
from app.mod_shift.controllers import mod_shift as shift_module

# Register blueprint(s)
# app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
app.register_blueprint(tech_module)
app.register_blueprint(category_module)
app.register_blueprint(shift_module)



# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()