from flask import Flask, render_template, request, jsonify, make_response
import json


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
