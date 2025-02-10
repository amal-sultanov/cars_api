from fastapi import APIRouter
from pydantic import BaseModel

from api import result_message
from database.cars_services import (
    add_car_to_db,
    get_car_from_db,
    get_cars_from_db,
    update_car_in_db,
    delete_car_from_db
)

cars_router = APIRouter(prefix='/cars', tags=['cars'])


class CarCreate(BaseModel):
    name: str
    brand: str
    type: str
    engine_type: str
    transmission: str
    horsepower: int
    year: int
    price: float
    color: str


@cars_router.post('/add-car')
async def add_car(car_data: CarCreate):
    car_dict = dict(car_data)

    return result_message(add_car_to_db(**car_dict))


@cars_router.get('/get-car')
async def get_car(car_id: int):
    return result_message(get_car_from_db(car_id))


@cars_router.get('/get-cars')
async def get_cars():
    return result_message(get_cars_from_db())


@cars_router.put('/update-car')
async def update_car(car_id: int, target_info: str, new_info: str):
    return result_message(update_car_in_db(car_id, target_info, new_info))


@cars_router.delete('/delete-car')
async def delete_user(car_id: int):
    return result_message(delete_car_from_db(car_id))
