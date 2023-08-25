from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from config import DB_URL

Model = declarative_base(name = 'Model')
engine = create_engine(DB_URL)
Session = sessionmaker(engine, autoflush = False, autocommit = False)
