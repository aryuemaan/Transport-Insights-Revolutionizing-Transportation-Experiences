@app.route('/api/ride_data')
def get_ride_data():
    with open('ride_data.json', 'r') as file:
        ride_data = json.load(file)
    return jsonify(ride_data)

@app.route('/api/transportation_data')
def get_transportation_data():
    with open('transportation_data.json', 'r') as file:
        transportation_data = json.load(file)
    return jsonify(transportation_data)

@app.route('/api/delivery_data')
def get_delivery_data():
    with open('delivery_data.json', 'r') as file:
        delivery_data = json.load(file)
    return jsonify(delivery_data)
