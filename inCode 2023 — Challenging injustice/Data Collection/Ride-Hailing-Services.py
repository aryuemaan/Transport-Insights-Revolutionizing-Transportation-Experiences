import random

def simulate_ride_data(num_rides):
    ride_data = []
    for _ in range(num_rides):
        ride = {
            'duration': random.randint(5, 60),  # Simulate trip duration between 5 and 60 minutes
            'route': 'Origin -> Destination',
            'driver_behavior': random.choice(['Safe', 'Aggressive']),
            'vehicle_condition': random.choice(['Good', 'Average', 'Poor']),
            'customer_feedback': random.choice(['Satisfied', 'Neutral', 'Unsatisfied'])
        }
        ride_data.append(ride)
    return ride_data

num_rides = 100
simulated_ride_data = simulate_ride_data(num_rides)
