
import os
import requests
from flask.globals import request
from google.cloud import datastore  
from flask import Flask, json, jsonify, render_template

app = Flask(__name__)
datastore_client = datastore.Client()
kind = 'event'

@app.route("/", methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        r = requests.get(url = f"https://wave43-webhelp-pgallucci.oa.r.appspot.com/get/{request.form['key']}")
        data = r.json()
        return render_template('display.html',
                                table_data=data)  
    return  render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 80)))