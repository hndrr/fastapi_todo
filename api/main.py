import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print(
        "INFO:     FastAPI running on http://localhost:8000/docs (Press CTRL+C to quit)"
    )

@app.get("/")
async def index():
    return {"message": "index"}


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, access_log=True)
