FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./.env /app/.env

RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
