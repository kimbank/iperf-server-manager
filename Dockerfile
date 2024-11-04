# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /usr/src/app

# Install iperf3 and other required system packages
RUN apt-get update && apt-get install -y iperf3 procps && apt-get clean

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./app ./app

# Expose the application port
## Flask server port
EXPOSE 5000
## iperf3 server port
EXPOSE 5201

# Command to run the app
CMD ["python", "./app/main.py"]
