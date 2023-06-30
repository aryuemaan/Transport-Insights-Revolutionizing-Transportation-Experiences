import json

# Load simulated ride data
with open('ride_data.json', 'r') as ride_file:
    ride_data = json.load(ride_file)

# Load simulated transportation data
with open('transportation_data.json', 'r') as transportation_file:
    transportation_data = json.load(transportation_file)

# Load simulated delivery data
with open('delivery_data.json', 'r') as delivery_file:
    delivery_data = json.load(delivery_file)
# Analyze ride data
total_duration = sum(ride['duration'] for ride in ride_data)
average_duration = total_duration / len(ride_data)

# Analyze transportation data
passenger_counts = [trip['passenger_count'] for trip in transportation_data]
average_passenger_count = sum(passenger_counts) / len(passenger_counts)

# Analyze delivery data
on_time_deliveries = [delivery for delivery in delivery_data if delivery['delivery_accuracy'] == 'On time']
on_time_delivery_percentage = (len(on_time_deliveries) / len(delivery_data)) * 100
