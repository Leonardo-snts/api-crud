# Use uma imagem oficial do Python
FROM python:3.10-slim

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Coleta arquivos estáticos
RUN python manage.py collectstatic --no-input

# Exponha a porta que será usada
EXPOSE 8080

# Comando para iniciar o servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "api_crud.wsgi"]
