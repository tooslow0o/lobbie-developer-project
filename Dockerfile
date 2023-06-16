# Dockerfile, Image, Container

FROM python:3.11.4-slim

#destination folder 2nd param, try without . and without /
ADD app.py ./api

# TODO packages
RUN pip install [packages]

CMD ["python", "./app.py"]