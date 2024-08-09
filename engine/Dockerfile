FROM python:3.12.4

WORKDIR /app

COPY . .

USER root

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]