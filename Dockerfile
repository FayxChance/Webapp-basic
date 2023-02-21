FROM python:3.12.0a5-buster

WORKDIR /app

COPY requirements.txt .

COPY flaskr/ ./flaskr/

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "-m", "flask", "--debug", "--app", "flaskr", "run", "--host", "0.0.0.0"]