# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . .

# Expose port 8080 for GCP
EXPOSE 8080

# Set the default port to Cloud Run's PORT environment variable
ENV PORT 8080

# Run the Flask application using the PORT environment variable
CMD ["python", "app.py"]
