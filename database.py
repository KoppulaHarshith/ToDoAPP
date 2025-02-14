from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://todo_app_oyvv_user:rg7i2SlvQOfbip9oNGF0esIWpjWqfbi6@dpg-cunhm9ogph6c73et8m9g-a/todo_app_oyvv'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
