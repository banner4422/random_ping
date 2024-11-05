# Use the official Python image from the Docker Hub
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY random_ping.py .

# Install any required Python libraries
RUN pip install requests

# Set default environment variable for the URL
ENV PING_URL=https://example.com

# Run the Python script with the URL from the environment variable
CMD ["python", "random_ping.py"]
