import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify
from embed import embed
from query import query
from get_vector_db import get_vector_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
TEMP_FOLDER = os.getenv('TEMP_FOLDER', './_temp')
os.makedirs(TEMP_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route('/embed', methods=['POST'])
def route_embed():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    embedded = embed(file)

    if embedded:
        return jsonify({"message": "File embedded successfully"}), 200

    return jsonify({"error": "File embedded unsuccessfully"}), 400

@app.route('/query', methods=['POST'])
def route_query():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "No query provided"}), 400

    user_query = data.get('query')
    print(f"Received query: {user_query}")  # Debugging log

    try:
        response = query(user_query)
        if response:
            print(f"Generated response: {response}")  # Debugging log
            return jsonify({"message": response}), 200
    except Exception as e:
        print(f"Error in query function: {str(e)}")  # Debugging log

    return jsonify({"error": "Something went wrong"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
