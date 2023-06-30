import matplotlib.pyplot as plt

# Visualize average trip duration
plt.bar(['Ride'], [average_duration])
plt.xlabel('Transportation Mode')
plt.ylabel('Average Trip Duration (minutes)')
plt.title('Average Trip Duration by Transportation Mode')
plt.show()

# Visualize passenger count distribution
plt.hist(passenger_counts, bins=10)
plt.xlabel('Passenger Count')
plt.ylabel('Frequency')
plt.title('Distribution of Passenger Counts')
plt.show()

# Visualize on-time delivery percentage
labels = ['On Time', 'Delayed']
sizes = [on_time_delivery_percentage, 100 - on_time_delivery_percentage]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('On-Time Delivery Percentage')
plt.show()
