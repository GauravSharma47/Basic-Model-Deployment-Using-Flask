from app import app
from flask import render_template,request
import numpy as np
import pickle
@app.route('/')
def index():
	return render_template('index.html',predicted="")
@app.route('/predict',methods=["POST"])
def predict():
	height=[float(request.form['height'])]
	print("this is height ",height)
	height=np.array(height).reshape(1,-1)
	model=pickle.load(open("model.sav",'rb'))
	prediction=model.predict(height)
	output = round(prediction[0], 2)
	return render_template('index.html',predicted="Weight should be around {}".format(output))
