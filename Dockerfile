# Etapa 1: Usar a imagem base Python mais recente (3.10)
FROM python:3.10-slim

# Etapa 2: Definir diretório de trabalho dentro do contêiner
WORKDIR /app

# Etapa 3: Copiar o requirements.txt e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Etapa 5: Expor a porta onde o Streamlit será executado
EXPOSE 8080

# Etapa 6: Comando para rodar a aplicação, usando a variável de ambiente PORT definida pelo Cloud Run
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
