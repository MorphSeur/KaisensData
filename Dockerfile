FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get clean && apt-get update

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]