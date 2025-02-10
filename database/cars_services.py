from database import get_db
from database.models import Car


def add_car_to_db(name, brand, type, engine_type, transmission,
                  horsepower, year, price, color):
    db = next(get_db())
    car = Car(name=name, brand=brand, type=type, engine_type=engine_type,
              transmission=transmission, horsepower=horsepower,
              year=year, price=price, color=color)

    db.add(car)
    db.commit()

    return True


def get_car_from_db(car_id):
    db = next(get_db())
    car = db.query(Car).filter_by(id=car_id).first()

    if car:
        return car
    return False


def get_cars_from_db():
    db = next(get_db())

    return db.query(Car).all()


def update_car_in_db(car_id, target_field, new_value):
    db = next(get_db())
    car = db.query(Car).filter_by(id=car_id).first()

    if car:
        if target_field == 'name':
            car.name = new_value
        elif target_field == 'brand':
            car.brand = new_value
        elif target_field == 'type':
            car.type = new_value
        elif target_field == 'engine_type':
            car.engine_type = new_value
        elif target_field == 'transmission':
            car.transmission = new_value
        elif target_field == 'color':
            car.color = new_value

        db.commit()

        return True
    return False


def delete_car_from_db(car_id):
    db = next(get_db())
    car_to_delete = db.query(Car).filter_by(id=car_id).first()

    if car_to_delete:
        db.delete(car_to_delete)
        db.commit()

        return True
    return False
