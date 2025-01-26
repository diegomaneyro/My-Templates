from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/login_crypto")
def login_crypto():
    return render_template('login_crypto.html')

@app.route("/login_future")
def login_future():
    return render_template('login_future.html') 

@app.route("/login_live") 
def login_live():
    return  render_template('login_live.html')

@app.route("/form")
def form():
    return render_template('form.html')