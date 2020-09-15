from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('front.html')

@app.route('/front.js')
def index():
    return send_from_directory('/','front.js')   