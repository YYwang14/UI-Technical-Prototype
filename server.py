from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/iso1')
def iso1():
    return render_template('iso1.html')

@app.route('/iso2')
def iso2():
    return render_template('iso2.html')

@app.route('/iso3')
def iso3():
    return render_template('iso3.html')

@app.route('/iso_quiz')
def iso_quiz():
    return render_template('iso_quiz.html')


@app.route('/shutter_1')
def shutter_1():
    return render_template('shutter_1.html')

@app.route('/shutter_2')
def shutter_2():
    return render_template('shutter_2.html')

@app.route('/shutter_3')
def shutter_3():
    return render_template('shutter_3.html')

@app.route('/shutter_4')
def shutter_4():
    return render_template('shutter_4.html')

@app.route('/shutter_5')
def shutter_5():
    return render_template('shutter_5.html')

@app.route('/shutter_quiz')
def shutter_quiz():
    return render_template('shutter_quiz.html')



@app.route('/aperture')
def aperture():
    # Render a template for the Aperture section
    return render_template('aperture.html')

if __name__ == '__main__':
    app.run(debug=True)
