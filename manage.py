import os 
from flask import Flask,redirect
@app.route("/")
def index():
    return redirect("www.pornhub.com",code=302)
