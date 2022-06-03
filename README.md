# api_yatube

Перед вами REST API для Yatube (https://github.com/Glaser1/yatube) - социальной сети для публикации личных дневников.


### Использованные технологии:
 Python 3.7, Django 2.2.16, DRF 3.12.4, PyJWT 2.1.0
 

### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Glaser1/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

```
GET /api/v1/posts/

Response:
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {}
   ]
}

POST /api/v1/posts/

Response:
{
 "text": "string",
 "image": "string",
 "group": 0
}

Request:
{
 "id": 0,
 "author": "string",
 "text": "string",
"pub_date": "2019-08-24T14:15:22Z",
 "image": "string",
 "group": 0
}

GET /api/v1/follow/

Response:
[
  {
    "user": "string",
    "following": "string"
  }
]

POST /api/v1/follow/

Request:
{
  "following": "string
}

Response:
{
  "user": "string",
  "following": "string"
}
