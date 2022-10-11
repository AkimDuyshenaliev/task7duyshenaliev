from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


counter = 0
name = "Akim Duyshenaliev"
app = FastAPI()


@app.get("/")
async def root():
    return { "counter": counter }


@app.get("/stat")
async def stat():
    global counter
    counter += 1 
    return { "counter": counter - 1 }


@app.get("/about")
async def about():
    return HTMLResponse(f"<h3> Hello , { name }</h3>")


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)