# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Create virtual environment and install dependencies
RUN python3 -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

# Expose port (ubah sesuai kebutuhan aplikasi Anda)
EXPOSE 5000

# Command to run the application
CMD ["sh", "-c", ". venv/bin/activate && python3 app.py"]
