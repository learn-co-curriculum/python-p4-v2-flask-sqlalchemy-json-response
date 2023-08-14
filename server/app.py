# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    return make_response(
        '<h1>Welcome to the pet directory!</h1>',
        200
    )


@app.route('/demo_json')
def demo_json():
    pet_json = '{"id": 1, "name" : "Fido", "species" : "Dog"}'
    return make_response(pet_json, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
