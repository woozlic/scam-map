# Карта скам-проектов в России

## Разработка

Создать файл .env и в нем указать токен от API Shodan

```
TOKEN_SHODAN=...
```

## Создание окружения

```
python3 -m venv venv/
. venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```
python src/main.py
```