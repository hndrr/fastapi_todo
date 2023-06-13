import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print(
        "INFO: FastAPI running on http://localhost:8000/docs (CTRL+C to quit)"
    )


@app.get("/")
async def index():
    return {"message": "index"}


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}


# Path_param & Query_param example
# http://localhost:8000/countries/Japan?city_name=Tokyo
@app.get("/countries/{country_name}")
async def country(country_name: str = 'japan', city_name: str = 'Tokyo'):
    return {"country_name": country_name, "city_name": city_name}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, access_log=True)
