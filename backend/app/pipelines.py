from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([('scaler', StandardScaler()), 
                        ('SVC', SVC(kernel='rbf'))])