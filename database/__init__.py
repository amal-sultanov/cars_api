from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_DATABASE_URI = 'sqlite:///cars.db'

engine = create_engine(SQL_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()
