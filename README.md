### Build docker image
``` docker build -t fastapi_duyshenaliev . ```
### Launch docker image
```docker run --name app -p 8000:8000 fastapi_duyshenaliev```

### Launch local project
```uvicorn main:app --reload```

### Download docker image
```docker pull akimduyshenaliev/task5duyshenaliev:latest```
### Launch docker-compose
```docker compose up -d```