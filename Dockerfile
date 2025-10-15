# Use the official Python image from the Docker Hub
FROM python:3.14.0-alpine

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY random_ping.py /app/

# Set default environment variable for the URL
ENV PING_URL=http://localhost:3000
ENV PING_INTERVAL=3600

# Run the Python script with the URL from the environment variable
CMD ["python", "random_ping.py"]
