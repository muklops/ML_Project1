FROM python:3.8-slim-buster

# Install minimal system deps
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI via pip (works on slim images)
RUN pip install --no-cache-dir awscli

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
