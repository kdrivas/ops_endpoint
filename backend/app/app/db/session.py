from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://db:pass@db/db_dev')

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
