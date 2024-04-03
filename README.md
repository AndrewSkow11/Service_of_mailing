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
Для кеширования запуск редиса обязателен, команды для установки и запуска ниже (в случае если не были установлены все записимости из requirements.txt)

```commandline
brew install redis
pip install redis

redis-server
```

Запуск рассылки из командной строки
```commandline
./manage.py run_mailing.py
```
[run_mailing.py](main%2Fmanagement%2Fcommands%2Frun_mailing.py)

## Автор 
Андрей Сковородников, https://github.com/AndrewSkow11
