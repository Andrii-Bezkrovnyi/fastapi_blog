from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # Обновленный импорт

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://myuser:mypassword@localhost:3306/mydatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  # Использование нового импорта

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
