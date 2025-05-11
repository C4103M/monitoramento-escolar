FROM python:3.11-slim

# Cria e define o diretório da aplicação
WORKDIR /app

# Copia as dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta da aplicação Flask
EXPOSE 5000

# Comando para iniciar o servidor
CMD ["python", "app.py"]
