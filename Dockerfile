FROM python:3.9.16-slim-bullseye

COPY . /byc-app
WORKDIR /byc-app


RUN pip install -r requirements.txt

CMD ["bash", "entrypoint.sh"]
