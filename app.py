# SETUP ##########################################
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for)
import pandas as pd
import json

app = Flask(__name__)

# HOME PAGE ######################################
@app.route("/")
def home():
    return render_template("index.html")

# TABLE ############################################
@app.route("/notebook")
def table():
    return render_template("Project_3.html")

# RUN ############################################
if __name__ == "__main__":
    app.run(debug=True)