from flask import Flask, request, jsonify
import json

file = 'nyc.geojson'

app = Flask(__name__)
data = json.load(open('data/nyc.geojson'))

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return jsonify(data)
    else:

        return jsonsify(data)

if __name__ == '__main__':
    app.run(debug=True)
