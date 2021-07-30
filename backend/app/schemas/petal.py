from pydantic import BaseModel

class PetalBase(BaseModel):
	sepal_length: float
	sepal_width: float
	petal_length: float
	petal_width: float
	prediction: float

class PetalCreate(PetalBase):
	pass

class Petal(PetalBase):
	id: int

	class Config:
		orm_mode = True