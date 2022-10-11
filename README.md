## Сборка докер-образа
``` docker build -t fastapi_skachkov . ```
## Запуск докер-образа
```docker run --name app -p 8000:8000 fastapi_skachkov```

## Локальный запуск проекта
```uvicorn main:app --reload```

## Скачивание докер-образа
```docker pull skrachin/task5-skachkov:fastapi_skachkov```
## Запуск докер-образа
```docker run --name app -p 8000:8000 skrachin/task5-skachkov:fastapi_skachkov```