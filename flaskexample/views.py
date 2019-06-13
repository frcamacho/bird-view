from flask import render_template
from flaskexample import app

@app.route('/')
@app.route('/template/heatmap_santamonica_bird.html')
def map_data():
    return render_template('heatmap_santamonica_bird.html')
