import fire

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import make_pipeline

def main():
  print('Start training...')
  data = pd.read_csv('../data/iris.csv')
  rest, train = train_test_split(data, test_size=0.20)
  valid, test = train_test_split(rest, test_size=0.5)

  pipeline = make_pipeline([StandardScaler(), SGDClassifier()])

  X_train, y_train = train.drop(['Id', 'Species'], axis=1), train.Species
  X_valid, y_valid = valid.drop(['Id', 'Species'], axis=1), valid.Species
  X_test, y_test = test.drop(['Id', 'Species'], axis=1), test.Species

  enc = OneHotEncoder()
  enc.fit(y_train)

  y_train_t = enc.transform(y_train)
  y_valid_t = enc.transform(y_valid)
  y_test_t = enc.transform(y_test)

  pipeline.fit(X_train)
  
  y_trn_pred = pipeline.predict(y_train_t)
  y_val_pred = pipeline.predict(y_valid_t)
  y_test_pred = pipeline.predict(y_test_t)

if __name__ == '__main__':
  fire.Fire(main)