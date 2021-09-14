# short_story_blog
short_story_blog

---
Сайт где пользователи с подтверждённой почтой пишут текстовые посты.
Подтверждение почты произходит через отправку письма с помошью Celery паралельно работе сайта.


## Запуск
1. Создадите *.env* файл с переменными окружения. В файле *env_template* пример для локального запуска.
2. Выполните  ```docker-compose up  ``` в директории проекта.

## Технологии
* Django
* PostgrSQL
* Gunicorn
* NGINX
* Docker
* Celery
* Redis
