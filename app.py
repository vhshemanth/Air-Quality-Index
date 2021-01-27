
import pandas as pd
import matplotlib.pyplot as plt
# importing the necessary dependencies
import pickle

from flask import Flask, render_template, request
from flask_cors import cross_origin
import os

app = Flask(__name__)  # initializing a flask app

model=pickle.load(open('randomforest_model.pkl','rb'))


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("home.html")

@app.route('/graph', methods=['POST', 'GET'])
@cross_origin()
def graph():
    if request.method == 'POST':
        value=request.form['data']
        df=pd.read_csv('Data/Real-Data/Real_Combine.csv')
        df[value].plot()
        plt.title("Overall in Year 2013-2020")
        plt.xlabel(value)
        plt.show()
        return render_template('home.html',grapph=plt.show())

@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():

    if request.method=='POST':
        T=int(request.form["T"])
        TM = int(request.form["TM"])
        Tm = int(request.form["Tm"])
        SLP=int(request.form["SLP"])
        H = int(request.form['H'])
        VV = int(request.form['VV'])
        V = int(request.form['V'])
        VM = int(request.form['VM'])

        output=model.predict([[T,TM,Tm,SLP,H,VV,V,VM]])

        return render_template('home.html',prediction=output)


if __name__=="__main__":
    app.run(debug=True)