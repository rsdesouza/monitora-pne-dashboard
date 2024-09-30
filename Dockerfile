# Etapa 1: Imagem base com Python
FROM python:3.9-slim

# Etapa 2: Definir diretório de trabalho dentro do contêiner
WORKDIR /app

# Etapa 3: Copiar o requirements.txt e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: Copiar o código da aplicação para o diretório de trabalho
COPY . .

# Etapa 5: Expor a porta onde o Streamlit será executado
EXPOSE 8501

# Etapa 6: Comando para rodar a aplicação
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
