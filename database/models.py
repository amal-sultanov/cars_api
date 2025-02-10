from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

from database import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    type = Column(String, nullable=False)
    engine_type = Column(String, nullable=True)
    transmission = Column(String, nullable=True)
    horsepower = Column(Integer, nullable=True)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    color = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
