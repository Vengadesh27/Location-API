from flask import Flask, request, jsonify
from modules.address import Address

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def connection():
    return 'pong'

@app.route('/address', methods=['POST']) 
def location():
    data = request.json 
    if not data or 'lat' not in data or 'long' not in data:
        return jsonify({"error": "Invalid input. Please provide 'lat' and 'long'."}), 400
    
    lat = data.get("lat")
    long = data.get("long")
    
    address = Address()
    location_address = address.location_address(lat, long)
    
    return jsonify({"address": str(location_address)})

if __name__ == '__main__':
    app.run(debug=True)
