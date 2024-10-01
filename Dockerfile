# Etapa 1: Usar a imagem base Python mais recente
FROM python:3.10-slim

# Etapa 2: Instalar dependências do sistema necessárias para compilar pacotes como NumPy
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libatlas-base-dev \
    liblapack-dev \
    libblas-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Etapa 3: Definir diretório de trabalho dentro do contêiner
WORKDIR /app

# Etapa 4: Copiar o requirements.txt e instalar as dependências Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Etapa 6: Expor a porta onde o Streamlit será executado
EXPOSE 8080

# Etapa 7: Comando para rodar a aplicação, usando a variável de ambiente PORT definida pelo Cloud Run
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
