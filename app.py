import os
from google.cloud import datastore  
from flask import Flask, jsonify

app = Flask(__name__)
datastore_client = datastore.Client()
kind = 'hello_world'

@app.route("/")
def hello_world():
    key = datastore_client.key(kind,'the_data')
    task = datastore_client.get(key)
    return  jsonify(task)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))