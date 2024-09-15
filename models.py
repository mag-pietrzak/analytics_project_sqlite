import logging
from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database_setup import Base

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Defining tables
class User(Base):
    __tablename__ = 'Users'
    user_id = Column(String(36), primary_key=True)
    first_name = Column(String(60))
    last_name = Column(String(90))
    address = Column(String(150))
    age = Column(Integer)
    email = Column(String(50))

    transactions = relationship('Transaction', back_populates='user')

class Product(Base):
    __tablename__ = 'Products'
    product_id = Column(String(36), primary_key=True)
    product_name = Column(String(100), unique=True)
    product_category = Column(String(100))
    product_type = Column(String(100))
    product_price = Column(Integer)

    transactions = relationship('Transaction', back_populates='product')

class Transaction(Base):
    __tablename__ = 'Transactions'
    transaction_id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey('Users.user_id'))
    product_id = Column(String(36), ForeignKey('Products.product_id'))
    transaction_date = Column(Date)

    user = relationship('User', back_populates='transactions')
    product = relationship('Product', back_populates='transactions')

logging.info("Tables defined.")