# Service_of_mailing
Сервис управления рассылками, администрирования и получения статистики.

## Применение 
- для удержания текущих клиентов
- вспомогательные, или «прогревающие», рассылки для информирования и привлечения клиентов

## Технологиии 
- Python 3 
- Django 5
- PostgreSQL

## Развёртывание проекта 
- скачать все файлы проекта
- установить зависимости из файла requirement.txt
- создать .env файл со своими файлами (образец приложен)
- создать базу данных
```commandline
(venv) % psql -U postgres 
Password for user postgres: 
postgres=# CREATE DATABASE db_mailer;
CREATE DATABASE
postgres=# \q
```

В случае возникновения ошибки InvalidCursorName 
```commandline
python3 manage.py migrate --run-syncdb

```


## Автор 
Андрей Сковородников, https://github.com/AndrewSkow11
