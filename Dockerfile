# Use the official Python image
FROM python:3.10

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

# Etapa 6: Comando para rodar a aplicação, usando a variável de ambiente PORT definida pelo Cloud Run
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
