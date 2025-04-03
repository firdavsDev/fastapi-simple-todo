# -*- coding: utf-8 -*-

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # Agar DB_TYPE aniqlanmasa, sqlite bo'ladi

if DB_TYPE == "postgresql":
    # PostgreSQL uchun connection string
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
else:
    # SQLite uchun connection string
    DB_NAME = os.getenv("DB_NAME", "sqlite_db.db")
    DATABASE_URL = f"sqlite:///{DB_NAME}"

# SQLAlchemy engine va session yaratish
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_database():
    try:
        Base.metadata.create_all(bind=engine)
        print("Database created successfully!")
    except Exception as e:
        print(f"Error creating database: {e}")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
