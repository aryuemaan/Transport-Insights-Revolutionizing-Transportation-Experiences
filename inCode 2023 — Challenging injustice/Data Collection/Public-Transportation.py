import random

def simulate_public_transportation_data(num_trips):
    transportation_data = []
    for _ in range(num_trips):
        trip = {
            'schedule': '08:00 AM - 09:00 AM',  # Simulate schedule time
            'stops': ['Stop A', 'Stop B', 'Stop C'],  # Simulate list of stops
            'delay': random.randint(0, 10),  # Simulate delay in minutes
            'passenger_count': random.randint(0, 50)  # Simulate passenger count
        }
        transportation_data.append(trip)
    return transportation_data

num_trips = 50
simulated_transportation_data = simulate_public_transportation_data(num_trips)
