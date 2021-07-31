from fastapi import APIRouter, Form, File, UploadFile, Depends
from joblib import load

from sqlalchemy.orm import Session
import codecs
import csv
import pandas as pd

from . import deps
from app import crud, schemas

pipeline_pkl = load('pipeline.joblib')

router = APIRouter(
	prefix="/petals",
	tags=["petals"],
  responses={404: {"description": "Not found"}},
)

@router.get("/")
def ping():
	return {"petals": "I'm alive"}

@router.get('/dummy_pred')
def get_dummy(db = Depends(deps.get_session)):
	sample = [[5.1,3.5,1.4,0.2]]
	pred = pipeline_pkl.predict(sample)[0]

	petal = schemas.petal.PetalCreate(sepal_length=1, sepal_width=2, petal_width=3, petal_length=4, prediction=5)
	#petal. = 1
	#petal.sepal_width = 2
	#petal.petal_width = 4
	#petal.petal_length = 3
	#petal.prediction = 5

	crud.petal.create_petal(db, petal)

	return {"pred_dummy": int(pred)}

@router.post('/pred_sample/')
def predict_sample(sepal_length:float = Form(...),
									sepal_width:float = Form(...),
									petal_length:float = Form(...),
									petal_width:float = Form(...)):
	sample = [[sepal_length, sepal_width, petal_length, petal_width]]
	pred = pipeline_pkl.predict(sample)[0]

	petal = schemas.petal.PetalCreate(1,2,3,4,5)
	crud.petal.create_petal(db, petal)

	return {"prediction": int(pred)}

@router.post('/pred_batch/')
def predict_batch(file:UploadFile = File(...)):
	data = pd.DataFrame(csv.reader(codecs.iterdecode(file.file, 'utf-8')))
	preds = [float(v) for v in pipeline_pkl.predict(data)]

	# To-do: Write in Redis

	return {"predictions": preds}