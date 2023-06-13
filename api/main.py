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

# Path_param example
# http://localhost:8000/countries/Japan
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}

# Query_param example
# http://localhost:8000/countries?country_name=Japan
@app.get("/countries")
async def country(country_name: str = 'japan', country_id: str = 'jp'):
    return {"country_name": country_name, "country_id": country_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, access_log=True)
