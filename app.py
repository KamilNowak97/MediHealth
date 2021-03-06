from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('templates\config.py')

db = SQLAlchemy(app)

from templates.routes.routes import *
if __name__ == "__main__":
    app.run(debug=True)
