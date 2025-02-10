from fastapi import FastAPI

from api.cars import cars_router
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(docs_url='/')
app.include_router(cars_router)
