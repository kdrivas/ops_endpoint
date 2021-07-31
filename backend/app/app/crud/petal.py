from sqlalchemy.orm import Session
from app.models.petal import Petal
from app.schemas.petal import PetalCreate

def get_petals(db: Session, skip:int = 0, limit:int = 100):
	return db.query(Petal).offset(skip).limit(limit)

def create_petal(db:Session, petal: PetalCreate):
	db_user = Petal(**petal.dict())
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user