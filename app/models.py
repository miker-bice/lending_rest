from .database import Base
from sqlalchemy import Column, Integer, String, Float, null
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from datetime import datetime

class Loans(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fist_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    desired_loan_amount = Column(Float, nullable=False)
    loan_term = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now())
    # created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now())