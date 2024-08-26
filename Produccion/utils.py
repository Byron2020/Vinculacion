import pandas as pd
import numpy as np
import sklearn
import joblib

#escalamiento
class Utils:
    def load_from_excel(sleft, path):
        return pd.read_excel(path)
    
    def load_from_mysql(self):
        pass

    def features_target(self, dataset, drop_cols, y):
        X=dataset.drop(drop_cols,axis=1)
        y=dataset[y]
        return X,y
    
    def model_export(self,clf, score):
        print(score)
        joblib.dump(clf,'./models/mejor_modelo_'+str(round(score,3))+'.pkl')