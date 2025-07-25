from sqlalchemy import Column, Integer, String, BigInteger
from db import db_manager

Base = db_manager.Base

class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    population = Column(BigInteger, nullable=False) 