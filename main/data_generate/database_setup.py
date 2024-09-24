import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
database_url = 'sqlite:///data_generate/database/fake_online_shop.db'
no_rec = 6000

# Define database schema
Base = declarative_base()
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

# Create database and tables
def create_database():
    Base.metadata.create_all(engine)
    logging.info("Database and tables created.")