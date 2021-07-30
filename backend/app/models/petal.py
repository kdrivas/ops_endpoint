from sqlalchemy import Column, Integer, Float
from sqlalchemy.sql.expression import null
from app.db.base_class import Base

class Petal(Base):
	__tablename__ = "petals"

	id = Column(Integer, primary_key=True, index=True)	
	sepal_length = Column(Float, nullable=False)
	sepal_width = Column(Float, nullable=False)
	petal_length = Column(Float, nullable=False)
	petal_width	= Column(Float, nullable=False)
	prediction = Column(Float, nullable=False)
