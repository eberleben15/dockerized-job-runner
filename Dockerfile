# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the local directory into the container's /app directory
COPY . .

# Add execute permissions to all necessary scripts
RUN chmod +x /app/src/main.py

# Command to run the application
CMD ["python", "src/main.py"]