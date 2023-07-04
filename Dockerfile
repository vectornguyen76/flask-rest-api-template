FROM python:3.9-slim

# Install nmap
RUN apt-get update && apt-get install -y nmap

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Chmod to entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]