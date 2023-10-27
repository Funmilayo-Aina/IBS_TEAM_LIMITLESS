## Import libraries and creating flask app

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import sklearn
import numpy as np
import pandas as pd

app = Flask(__name__)

## loading the saved model
model = pickle.load(open("model.pkl","rb"))

@app.route('/', methods=['GET'])

def home():
    return render_template("index.html")

@app.route("/Predict",methods=["POST"])

def predict():
    if request.method == 'POST':
       # Stem_lenght = float(request.form['Stem_lenght'])        
        Root_lenght = float(request.form['Root_lenght'])
        Stem_diameter = float(request.form['Stem_diameter'])
        Chlorophyll = float(request.form['Chlorophyll'])
        Above_Ground_Dry_Weight = float(request.form['Above_Ground_Dry_Weight'])
        Above_Ground_Fresh_Weight = float(request.form['Above_Ground_Fresh_Weight'])
        N = float(request.form['N'])
        P = float(request.form['P'])
        Ca = float(request.form['Ca'])
        Mg = float(request.form['Mg'])
        CEI = float(request.form['CEI'])
        
        float_features = [[Root_lenght,Stem_diameter,Chlorophyll,Above_Ground_Dry_Weight,Above_Ground_Fresh_Weight,N,P,Ca,Mg,CEI]]
        #float_features = [float(x) for x in request.form.values()]
        print(float_features)
        features = [np.array(float_features)]
        make_prediction = model.predict(features[0])
        print(make_prediction)
        if make_prediction<0:
            return render_template('index.html', prediction_text="Sorry, you cannot have negative value")
        else:
            return render_template('index.html', prediction_text="The Stem Lenght would be {}".format(make_prediction))
        
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)

