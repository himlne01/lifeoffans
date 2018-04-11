from flask import Flask, url_for, redirect, render_template, request, Response, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def contact("/"):
    return render_template('contact.html')
