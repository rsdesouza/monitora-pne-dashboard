# Use the official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Atualizar e instalar pacotes necessários
RUN apt-get update && apt-get install -y \
    python3-setuptools \
    python3-wheel \
    build-essential \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Instalar setuptools manualmente (para garantir)
RUN pip install --upgrade pip setuptools wheel

# Copiar o arquivo requirements.txt e instalar dependências
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
