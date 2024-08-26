import joblib #Bilbioteca para Flash
import numpy as np

from flask import Flask, request
from flask import jsonify
from sklearn.linear_model import LinearRegression

app= Flask(__name__)


#POSTMAN PARA PRUEBAS
@app.route('/predict',methods=['GET'])
def predict():
    X_test= np.array([2.558,0.1,0.1255,0.128])
    prediction=model.predict(X_test.reshape(1,-1))
    return jsonify({'predicion': list(prediction)})


if __name__=="__main__":
    model=joblib.load('./models/mejor_modelo_0.883.pkl')
    app.run(port=8080)