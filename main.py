from flask import Flask, json, jsonify, request
from flask_cors import CORS
import pandas as pd

data = pd.read_csv('star_data.csv')
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "Success!"
    }), 200


@app.route("/star")
def star():
    name = request.args.get("name")
    star_data  = next(item for item in data if item["name"]==name )
    return jsonify({
        "data": star_data,
        "message": "Success!"
        
    }),200

if(__name__ == "__main__"):
    app.run(debug=True)