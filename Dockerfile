FROM python:3.8

COPY server.py /app/server.py

WORKDIR /app

EXPOSE 8080

CMD ["python", "server.py"]