# Inatel - Teste Técnico

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/16121141b3714f099e645f7e7c310651)](https://www.codacy.com/gh/vinigracindo/inatel/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vinigracindo/inatel&amp;utm_campaign=Badge_Grade)

## Sistema de Registro de Manutenção de Antenas

## Requerimentos
1. Django >= 4.0
2. Python >= 3.10
3. Pipenv >= 2021.5
4. PostgresSQL >= 9.4

## Como fazer deploy via docker?
1. Clone o repositório.
```console
git clone https://github.com/vinigracindo/inatel.git inatel
cd inatel
```

2. Crie um arquivo .env de configuração.
```console
cp .env.example .env
```

3. Dê permissão de chmod para o arquivo .docker/entrypoint.sh
```console
chmod +x .docker/entrypoint.sh
```

4. Execute o docker-composer
```console
docker-compose up -d
```

5. Acesse na porta 8000. Usuário: admin, Senha: admin
```console
http://localhost:8000
```

## Como desenvolver?

1. Clone o repositório.
```console
git clone https://github.com/vinigracindo/inatel.git inatel
cd inatel
```
2. Crie um arquivo .env de configuração.
```console
SECRET_KEY='django-insecure-f_+brylq@z!($$^)13n=^!u@uvi7tt=+1sh3sv=zzz46l5qgn^'
DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost;127.0.0.1
WEATHER_API_KEY=6d56fbaae0f53bd1fa246a8860c8fb04
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=inatel-db
SQL_USER=inateluser
SQL_PASSWORD=inatel123456
SQL_HOST=localhost
SQL_PORT=5432
SQL_LOG_ENGINE=django.db.backends.postgresql
SQL_LOG_DATABASE=inatel-log-db
SQL_LOG_USER=inateluser
SQL_LOG_PASSWORD=inatel123456
SQL_LOG_HOST=localhost
SQL_LOG_PORT=5432
```
3. Instale as dependências.
```console
pipenv install
```
4. Execute as migrações.
```console
pipenv run python manage.py migrate
```
5. Realize os testes.
```console
pipenv run python manage.py test
```
6. Crie um super usuário.
```console
pipenv run python manage.py createsuperuser
```
7. Inicie o servidor.
```console
pipenv run python manage.py runserver
```