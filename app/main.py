from fastapi import Depends, FastAPI
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware

from app.routers import courses
where_am_i = os.environ.get("WHEREAMI", None)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


app.include_router(courses.router)


@app.get('/')
def hello_world():
    global where_am_i

    if where_am_i is None:
        where_am_i = "NOT IN DOCKER"

    return f"Hello, from {where_am_i}! I changed and I'm microservice 3."


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



