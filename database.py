from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER_NAME = "postgres"
PASSWORD = "this"
SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_NAME}:{PASSWORD}@127.0.0.1:5432/crud_db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
