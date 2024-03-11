# Как запустить проект

1. Запускаем Docker Compose:

   ```bash
   docker compose up
   ```
2. Выполняем миграции:
   ```bash
   docker compose exec backend python manage.py migrate
   ```
## Примеры запросов к API

1. Создание организации:

   ```bash
   POST api/organizations/
   {
      "title":"test title",
      "description":"test description",
      "address":"test address",
      "postcode":"test postcode"
   }
   ```
   
2. Создание мероприятия:

   ```bash
   POST api/organizations/
   {
      "title":"test title",
      "description":"test description",
      "organizations": [
        "test organization 1",
        "test organization 2"
      ],
      "date": "2015-01-01",
      "image": "imagefile.jpg",
   }
   ```
3. Вывод мероприятий:

    ```bash
    GET api/events/
    ```

Теперь ваш проект должен быть доступен по адресу http://localhost:8000/.
Также по адресу http://localhost:5555 доступно возможность мониторинга тасок.

