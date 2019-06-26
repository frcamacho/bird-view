from flask import render_template
from flaskexample import app

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/map')
def map_data():
    return render_template('heatmap_santamonica_bird.html')

@app.route('/BirdView')
def BirdView():
    return render_template('location_form.html')
