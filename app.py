from flask import Flask, render_template, request
import flask
import footprint as fp

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/carbonfootprint', methods=["GET", "POST"])
def carbonfootprint():
    if flask.request.method == 'POST':
        type = request.form.get('type') 
        persons = float(request.form.get('persons'))
        country = request.form.get('country')  
        origin = request.form.get('origin')  
        destination = request.form.get('destination')
        originf= str(origin) + " " + str(country)
        destinationf= str(destination) + " " + str(country)
        if type=="diesel_car":
            result = fp.diesel_car(persons,originf,destinationf)
        elif type=="petrol_car":
            result = fp.petrol_car(persons,originf,destinationf)
        elif type=="motorcycle":
            result = fp.motorcycle(persons,originf,destinationf)
        elif type=="bus":
            result = fp.motorcycle(persons,originf,destinationf)
    return render_template('carbonfootprint.html', **locals())

