FROM python:3.12.4

WORKDIR /app

COPY . .

USER root

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "main.py", "--server.port", "80"]