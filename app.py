from datetime import datetime
from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)

number = 0

@app.route("/")
def date():
    return render_template(
    "part_one.html",
    now = datetime.now()
    )
@app.route("/start")
def start():
    return render_template(
    "part_two.html", 
    
    )
@app.route("/calculate")
def calc():
    number = request.form.get('userInput')
    return(number)