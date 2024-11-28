# API CRUD - Django REST Framework

## Descrição:

Uma API desenvolvida em Django REST Framework para gerenciar operações CRUD. Este projeto pode ser integrado a uma aplicação React e suporta implantação com Docker e foi hospedad no Google Cloud, armazena dados em um banco de dados postgresql e transferi os dados para o local chamado.

## Requisitos:

- Python 3.10 ou superior
= Django 5.1 ou superior
- Django REST Framework
- Docker (opcional, para containerização)
- Google Cloud SDK (opcional, para deploy)

## Instalação:

### 1. Clone o repositório:

```
git clone https://github.com/Leonardo-snts/api-crud.git
cd api-crud
```

### 2. Crie e ative um ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências:

```
pip install -r requirements.txt
```

### 4. Configuração do banco de dados:

  Crie um arquivo .env e coloque as credencias de acesso ao banco de dados nele como no exemplo do projeto que usa postgresql

```
DB_NAME=nome-do-banco
DB_USER=usuário
DB_PASSWORD=senha-de-acesso
DB_HOST=Host-do-db
DB_PORT=porta-usada
```

### 5. Execute as migrações:

 ```
python manage.py migrate
```

### 6. Inicie o servidor:

 ```
python manage.py runserver
```
Após iniciar o servidor, a API estará disponível em http://127.0.0.1:8000/

## Uso com Docker e Docker-compose 

### Docker
Build da imagem Docker:

 ```
docker build -t django_app .
 ```

Execute o container:

 ```
docker run -p 8080:8080 django_app
 ```

### Docker-compose

 ```
docker compose up -d --build
 ```

Após iniciar o docker ou docker compose, a API estará disponível em http://127.0.0.1:8080/
