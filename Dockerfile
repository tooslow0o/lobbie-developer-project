# Dockerfile, Image, Container

FROM python:3.11.4-slim

ADD app.py .

# TODO packages
RUN pip install [packages]

CMD ["python", "./app.py"]