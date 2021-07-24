from fastapi import FastAPI
from joblib import load

app = FastAPI()
pipeline_pkl = load('pipeline.joblib')

@app.get('/')
def root():
	return {"message": "I'm alive"}

@app.get('/dummy_pred')
def get_dummy():
	sample = [[5.1,3.5,1.4,0.2]]
	pred = pipeline_pkl.predict(sample)
	return {"pred_dummy": pred}