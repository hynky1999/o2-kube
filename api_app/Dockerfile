# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

RUN pip install --no-cache-dir flask

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run api.py when the container launches
CMD ["python", "app.py"]
