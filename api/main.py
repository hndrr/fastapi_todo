from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print(
        "INFO:     FastAPI running on http://localhost:8000/docs (Press CTRL+C to quit)"
    )


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
