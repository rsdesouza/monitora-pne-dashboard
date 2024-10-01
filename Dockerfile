# Use the official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Install system dependencies needed for numpy and other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    python3-distutils \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . .

# Expose port 8080 for GCP
EXPOSE 8080

# Set the default port to Cloud Run's PORT environment variable
ENV PORT 8080

# Run the application using the PORT environment variable
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
