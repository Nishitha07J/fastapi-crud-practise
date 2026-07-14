from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:nishitha@localhost:5432/Laddu"
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit = False,autoflush = False, bind = engine)
