# Import Packages
import pickle
import urllib.request as request

import flask
import numpy as np
import pandas as pd
from flask import Flask, request, url_for, redirect, render_template, jsonify

filename = '/Users/bintualkassoum/Downloads/final_model.pkl'
rooms_model = pd.read_pickle(filename)

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list: object) -> object:
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open('/Users/bintualkassoum/Downloads/final_model.pkl', 'rb'))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/predict', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        prediction = str(result)
        return render_template('predict.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
