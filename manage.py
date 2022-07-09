import os
from flask import Flask,redirect


@app.route("/")
def index():
return redirect("http://www.example.com", code=302)
