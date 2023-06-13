from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_lobbie():
    return 'Hello, Lobbie!'

    # TODO
@app.route('/file')
def get_file():
    return 'false'

    # TODO
@app.route('/files')
def get_prev_gen_files():
    return 'false'

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
#       Cpip install flask-sqlalchemy
#       pip install flask-restful


