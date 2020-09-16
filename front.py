from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/home')
def index():
    resp = make_response(render_template('front.html'))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return render_template('front.html')

