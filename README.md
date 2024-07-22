
# Тестовое задание Python **Developer** # Weather_app

Сделать web приложение, оно же сайт, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

    Стэк технологий: Django, requests, python-dotenv, unittest

Данные о погоде: [`www.visualcrossing.com`](https://www.visualcrossing.com/)

### Для запуска локально:

 1. Склонировать репозиторий
 2. Установить виртуальное окружение и активировать его
	```bash
	python -m venv venv
	source venv/scripts/activate
	```
 3. Перейти в корневой каталог приложения и создать файл для переменных окружения: `.env`
	```bash
	cd app
	```
	```bash
	  ->|-app
	    | |-app
	    | |-templates
	    | |-weather
	    | |-...
	    |-env.example
	    |-.env <--
	```
 4. Скопировать настройки из `env.example` в `.env`
  (Для работы с внешним API необходим `api_key`, можно использовать тот что указан в `env.example`)
 5. Установить зависимости
	```bash
	pip install -r requirements.txt
	```
 6. Запустить проект
	```bash
	python manage.py runserver
	```

### Для запуска в Docker-контейнере:

 1. Из локального запуска использовать пункты 1, 2, 3 и 4
 2. Собрать Docker-build
	```bash
	docker-compose build
	```
 3. Запустить Docker-compose
	```bash
	docker-compose up
	```
 
 Доступ к проекту: [127.0.0.1:8000](http://127.0.0.1:8000/)

Для простоты развёртывания проекта, при тестировании, использовалась библиотека `unittest`, так как БД в данном проекте не использовалась.

### Для запуска тестов:
Из корневого каталога приложения выполнить команду:
```bash
python manage.py test
```
