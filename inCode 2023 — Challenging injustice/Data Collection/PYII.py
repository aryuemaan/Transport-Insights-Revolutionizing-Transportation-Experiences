import random

def simulate_delivery_data(num_deliveries):
    delivery_data = []
    for _ in range(num_deliveries):
        delivery = {
            'duration': random.randint(15, 120),  # Simulate delivery duration between 15 and 120 minutes
            'route': 'Origin -> Destination',
            'delivery_accuracy': random.choice(['On time', 'Delayed']),
            'customer_feedback': random.choice(['Excellent', 'Good', 'Average'])
        }
        delivery_data.append(delivery)
    return delivery_data

num_deliveries = 50
simulated_delivery_data = simulate_delivery_data(num_deliveries)
