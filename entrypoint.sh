#!/bin/sh

echo "Esperando pelo banco de dados..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Banco de dados está acessível!"

python manage.py migrate

exec "$@"
