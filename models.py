from sqlalchemy import Column, Integer, String
from database import Base

class KpaData(Base):
    __tablename__ = "kpa_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    phone = Column(String(15))
