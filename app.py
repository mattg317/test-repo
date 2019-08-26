from flask import Flask
import json

file = 'nyc.geojson'

app = Flask(__name__)

@app.route('/')
def index():
    data = json.load(open('data/nyc.geojson'))
    return data

if __name__ == '__main__':
    app.run(debug=True)
