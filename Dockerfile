FROM python:3.10

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gfortran \
    libatlas-base-dev \
    libblas-dev \
    liblapack-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Atualizar o pip
RUN pip install --upgrade pip

# Instalar as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Etapa 5: Expor a porta onde o Streamlit será executado
ENV PORT 8080

# No comando de execução da aplicação (streamlit run), certifique-se de incluir a porta 8080
CMD streamlit run app.py --server.port $PORT --server.headless true
