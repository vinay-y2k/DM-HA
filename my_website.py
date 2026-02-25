import pandas as pd
from flask import Flask, request, jsonify, send_file
import os
from flask_compress import Compress
# import pinggy


# # Start an HTTP tunnel forwarding traffic to localhost on port 8000
# tunnel = pinggy.start_tunnel(forwardto="localhost:5000")

# print(f"Tunnel started. Urls: {tunnel.urls}")

VALID_API_KEY = os.environ.get('MY_API_KEY')

app = Flask(__name__)
Compress(app)

@app.route('/')
def index():
    response = "<h1> My first page <h1>"
    return response

@app.route('/get-data')
def get_data():
    file_path = r'/app/DM-HA/project1_df.csv'
    # Capture URL parameter: 
    output_format = request.args.get('output')
    user_key = request.headers.get('X-API-KEY')

    if user_key != VALID_API_KEY:
        return jsonify({"error":"Invalid API key"}),401
    
    if output_format == 'json':
        # Load CSV and convert to JSON format
        df = pd.read_csv(file_path)
        # 'records' orientation creates a list of row objects
        json_data = df.to_dict(orient='records')
        return jsonify(json_data)
    else:
        # Default behavior: deliver the actual CSV file
        return send_file(file_path, mimetype='text/csv')
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,ssl_context=('cert.pem','key.pem'))   

