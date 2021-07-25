from fastapi import FastAPI, Form, File, UploadFile
from joblib import load
from io import StringIO
from starlette.middleware.cors import CORSMiddleware

import codecs
import csv
import pandas as pd

pipeline_pkl = load('pipeline.joblib')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
	return {"message": "I'm alive"}

@app.get('/dummy_pred')
def get_dummy():
	sample = [[5.1,3.5,1.4,0.2]]
	pred = pipeline_pkl.predict(sample)[0]

	return {"pred_dummy": int(pred)}

@app.post('/pred_sample/')
def predict_sample(sepal_length:float = Form(...),
									sepal_width:float = Form(...),
									petal_length:float = Form(...),
									petal_width:float = Form(...)):
	sample = [[sepal_length, sepal_width, petal_length, petal_width]]
	pred = pipeline_pkl.predict(sample)[0]

	# To-do: Write in Redis

	return {"prediction": int(pred)}

@app.post('/pred_batch/')
def predict_batch(file:UploadFile = File(...)):
	data = pd.DataFrame(csv.reader(codecs.iterdecode(file.file, 'utf-8')))
	preds = [float(v) for v in pipeline_pkl.predict(data)]

	# To-do: Write in Redis

	return {"predictions": preds}