import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

# creating instance
app=Flask(__name__)

# tell flask what url should trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    # Generating HTML from within Python
    return flask.render_template('index.html')
    

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    # get the input data from html
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        
        if int(result)==1:
            prediction='Income more than 50K'
        else:
            prediction='Income less that 50K'
        
	# return the result to result.html with its prediction
        return render_template("result.html",prediction=prediction)

if __name__ == "__main__":
	app.run(debug=True)
