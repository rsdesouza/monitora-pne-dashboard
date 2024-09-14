# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para a pasta de trabalho
COPY requirements.txt .
COPY app/estrategias.csv .
COPY app/main.py .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Executa a aplicação Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.enableCORS=false"]
