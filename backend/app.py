from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from results import getResults

@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('q')
    results = getResults(query);
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')