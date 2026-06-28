import os 
import pymongo
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['serverstorage']

app = Flask(__name__)

# --- NEW: Create a dummy backend file if it doesn't exist ---
BACKEND_FILE = "backend_data.txt"
if not os.path.exists(BACKEND_FILE):
    with open(BACKEND_FILE, "w") as f:
        f.write(" john wick: the goat, spidermon : new day , something:ignore, ")

# 1. New /api route reading data from a backend file
@app.route('/api', methods=['GET'])
def get_file_data():
    try:
        with open(BACKEND_FILE, "r") as f:
            content = f.read()
        # Splitting the string into a clean JSON list
        data_list = [item.strip() for item in content.split(",") if item]
        return jsonify(data_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.json)
        # Simple validation: don't allow empty names
        if not form_data.get('name'):
            return jsonify({"error": "Name field cannot be empty!"}), 400
            
        collection.insert_one(form_data)
        return jsonify({"message": "Data submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500


@app.route('/view')
def view():
    raw_data = list(collection.find())
    for item in raw_data:
        if '_id' in item:
            item['_id'] = str(item['_id'])
    
    return {"data": raw_data}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)