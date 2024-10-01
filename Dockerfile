# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire app
COPY . .

# Expose port 8080 for GCP
EXPOSE 8080

# Run Streamlit on port 8080 (Cloud Run expects this)
CMD streamlit run app.py --server.port 8080 --server.enableCORS false
