from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# create an instance of Flask
app = Flask(__name__)

# do not run this if it's called elsewhere
if __name__ == "__main__":
    app.run()

# create an API object for flask-restful
api = Api(app)

# connect to the database if it exists
# if not, create a new db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////emp.db'
# remove flask server warning
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

# sqlalchemy mapper
db = SQLAlchemy(app)

# class
class 

@app.route('/')
def hello_lobbie():
    return 'Hello, Lobbie!'

    # TODO
#@app.route('/file')
#def get_file():
#    return 'false'

    # TODO
#@app.route('/files')
#def get_prev_gen_files():
#    return 'false'

### Requirements
# Each docker container must include a Flask API.
# The Flask API should have a route at `/file` that returns the name of a randomly-named and dynamically-generated txt file that is located within the docker container. *When* the file is generated is up to you and different docker containers should return different files from this endpoint.
# The Flask API should have a route at `/files` that returns a list of all previously generated files. The randomly-named generated file should not be present.
# Destroying and creating a docker container should result in a different randomly-named file returned from `/file` and a list of files from other containers that were previously run from `/files`.
# Unit tests for any python code you write.


## Create Venv
#       python -m venv ~/VENVS/lobbie-developer-project/

## Activate Venv
#       ~/VENVS/lobbie-developer-project/Scripts/activate.bat

## Install PIP    ## Unnecessary, already installed and/or added by creating VENV

#       pip install flask
#       pip install flask-sqlalchemy
#       pip install flask-restful
#       pip install python-dotenv


