# Use uma imagem oficial do Python
FROM python:3.10-slim

# Configure o diretório de trabalho
WORKDIR /app

# Instale dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copie apenas o arquivo de dependências primeiro (para cache eficiente)
COPY requirements.txt /app/requirements.txt

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do projeto
COPY . /app

# Exponha a porta que será usada
EXPOSE 8080

# Comando para iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && gunicorn myproject.wsgi:application --bind 0.0.0.0:8080"]

