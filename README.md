# Service_of_mailing
Сервис управления рассылками, администрирования и получения статистики.

## Применение 
- для удержания текущих клиентов
- вспомогательные, или «прогревающие», рассылки для информирования и привлечения клиентов

## Технологиии 
- Python 3 
- Django 4
- PostgreSQL
- Redis

## Развёртывание проекта 
- скачать все файлы проекта
- установить зависимости из файла requirement.txt
- создать .env файл со своими файлами (образец приложен)
- создать базу данных
- создать и применить миграции
- сделать загрузку данных из db.json
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
Для кеширования запуск redis обязателен, т.к. из него попадает информация на главную страницу.

Команды для установки и запуска ниже (в случае если не были установлены все записимости из requirements.txt)

```commandline
brew install redis
pip install redis

redis-server
```

Запуск сервиса рассылок по расписанию
```commandline
./manage.py run_mailing.py
```


## Автор 
Андрей Сковородников, https://github.com/AndrewSkow11
