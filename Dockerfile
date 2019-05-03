FROM python:alpine3.9

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT [ "python", "./app.py" ]