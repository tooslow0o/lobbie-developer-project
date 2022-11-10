# Lobbie Developer Project

Before You Start
--------------------
Fork this repo!

Goal
--------------------
Build a tool that deploys a Flask API using Docker. 

### Requirements
* Each docker container must include a Flask API.
* The Flask API should have a route at `/file` that returns the name of a randomly-named and dynamically-generated txt file that is located within the docker container. *When* the file is generated is up to you and different docker containers should return different files from this endpoint.
* The Flask API should have a route at `/files` that returns a list of all previously generated files. The randomly-named generated file should not be present.
* Destroying and creating a docker container should result in a different randomly-named file returned from `/file` and a list of files from other containers that were previously run from `/files`.
* Unit tests for any python code you write.

### Tips
* For an example of how to create a randomly generated file, see the `random-file.sh` file.

### Instructions
Feel free to solve this any way you like, including using any libraries you would like. Some resources that you may find necessary or helpful include:

* Python venv module - https://docs.python.org/3/library/venv.html - for preventing system installation of dependencies.
* Flask - https://flask.palletsprojects.com/en/1.1.x/
* Docker - https://docs.docker.com/
* Docker Compose - https://docs.docker.com/compose/
* docker-py - https://docker-py.readthedocs.io/en/stable/

What You're Given
--------------------
NOTE: Feel free to modify any or all of the files listed here.

* An `api` directory with [A Minimal Flask Application](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)
* An empty `tests` directory.
* A requirements.txt with `Flask` as the only current dependency.
* A shell script called `random-file.sh`, which generates an empty txt file with name like "include-me-<random-string>".
* A .gitignore
* This README

What We Suspect You'll Add
--------------------
At a *minimum* we suspect that your project will add the below to list of files that you are given.

* A Dockerfile
* Instructions and possibly a script detailing how we can run your solution.
* Tests for python code.

Final Note
--------------------
There are a few different ways to solve this project. Feel free to solve it in as many ways as you would like, just be prepared to discuss why you might prefer one solution over another. Finally, please send us any questions you have if something isn't clear.
