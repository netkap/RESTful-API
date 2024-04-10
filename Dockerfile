FROM python:3.9-slim-buster
WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV host=0.0.0.0

EXPOSE 5000

RUN python3 -c "from app import db; db.create_all(); exit()"

# Start the application
CMD ["python3", "app.py"]