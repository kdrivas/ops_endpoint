from constants import LABEL_ENCODINGS
from pipelines import pipeline
import fire

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

from joblib import dump, load

def main():
  print('Start training...')
  data = pd.read_csv('../data/iris.csv')
  data['Species'] = data['Species'].replace(LABEL_ENCODINGS)

  rest, train = train_test_split(data, test_size=0.20)
  valid, test = train_test_split(rest, test_size=0.5)

  X_train, y_train = train.drop(['Id', 'Species'], axis=1), train.Species.values
  X_valid, y_valid = valid.drop(['Id', 'Species'], axis=1), valid.Species.values
  X_test, y_test = test.drop(['Id', 'Species'], axis=1), test.Species.values
  
  enc = LabelEncoder()
  enc.fit(y_train)

  pipeline.fit(X_train, y_train.reshape(-1,1))
  
  y_valid_pred = pipeline.predict(X_valid)
  y_test_pred = pipeline.predict(X_test)

  print('Macro average valid:', f1_score(y_valid, y_valid_pred, average='macro'))
  print('Macro average test:', f1_score(y_test, y_test_pred, average='macro'))

  # Serialize pipeline
  dump(pipeline, 'pipeline.joblib') 

if __name__ == '__main__':
  fire.Fire(main)