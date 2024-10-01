# Use a versão oficial estável do Python (3.10)
FROM python:3.10

# Set working directory
WORKDIR /app

# Atualizar e instalar pacotes necessários (inclui distutils, setuptools e wheel)
RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-setuptools \
    python3-wheel \
    build-essential \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Instalar setuptools e wheel manualmente
RUN pip install --upgrade pip setuptools==59.5.0 wheel==0.37.0

# Copiar o arquivo requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o app
COPY . .

# Expor a porta 8080 para o GCP
EXPOSE 8080

# Definir a variável de ambiente PORT usada pelo Cloud Run
ENV PORT 8080

# Comando para rodar a aplicação usando o Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
