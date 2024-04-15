from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/iso')
def iso():
    # Render a template for the ISO section
    return render_template('iso.html')

@app.route('/shutter_speed')
def shutter_speed():
    # Render a template for the Shutter Speed section
    return render_template('shutter_speed.html')

@app.route('/aperture')
def aperture():
    # Render a template for the Aperture section
    return render_template('aperture.html')

if __name__ == '__main__':
    app.run(debug=True)
