import random
import json

# Simulating Data Collection from Ride-Hailing Services
def simulate_ride_data(num_rides):
    ride_data = []
    for _ in range(num_rides):
        ride = {
            'duration': random.randint(5, 60),
            'route': 'Origin -> Destination',
            'driver_behavior': random.choice(['Safe', 'Aggressive']),
            'vehicle_condition': random.choice(['Good', 'Average', 'Poor']),
            'customer_feedback': random.choice(['Satisfied', 'Neutral', 'Unsatisfied'])
        }
        ride_data.append(ride)
    return ride_data

num_rides = 100
simulated_ride_data = simulate_ride_data(num_rides)

# Simulating Data Collection from Public Transportation
def simulate_public_transportation_data(num_trips):
    transportation_data = []
    for _ in range(num_trips):
        trip = {
            'schedule': '08:00 AM - 09:00 AM',
            'stops': ['Stop A', 'Stop B', 'Stop C'],
            'delay': random.randint(0, 10),
            'passenger_count': random.randint(0, 50)
        }
        transportation_data.append(trip)
    return transportation_data

num_trips = 50
simulated_transportation_data = simulate_public_transportation_data(num_trips)

# Simulating Data Collection from Delivery Companies
def simulate_delivery_data(num_deliveries):
    delivery_data = []
    for _ in range(num_deliveries):
        delivery = {
            'duration': random.randint(15, 120),
            'route': 'Origin -> Destination',
            'delivery_accuracy': random.choice(['On time', 'Delayed']),
            'customer_feedback': random.choice(['Excellent', 'Good', 'Average'])
        }
        delivery_data.append(delivery)
    return delivery_data

num_deliveries = 50
simulated_delivery_data = simulate_delivery_data(num_deliveries)

# Storing Simulated Data in JSON Files
with open('ride_data.json', 'w') as ride_file:
    json.dump(simulated_ride_data, ride_file)

with open('transportation_data.json', 'w') as transportation_file:
    json.dump(simulated_transportation_data, transportation_file)

with open('delivery_data.json', 'w') as delivery_file:
    json.dump(simulated_delivery_data, delivery_file)

""" we have defined functions to simulate data collection from ride-hailing services, public transportation, and delivery companies. The simulated data is then stored in separate JSON files (ride_data.json, transportation_data.json, and delivery_data.json) using the json.dump() function.

You can adjust the parameters and data points in the simulation functions as per your requirements. Additionally, you can modify the storage mechanism based on your preferred data storage and processing approach, such as using a database or cloud storage.

Remember to install the required Python libraries (e.g., json) before running the script. """