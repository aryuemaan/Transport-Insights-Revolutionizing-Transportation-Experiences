const express = require('express');
const app = express();
const mongoose = require('mongoose');
const { RideDataModel, DeliveryDataModel } = require('./models'); // Assuming you have defined Mongoose models for ride and delivery data

// Connect to the MongoDB database
mongoose.connect('mongodb://localhost:27017/transport-insights', { useNewUrlParser: true, useUnifiedTopology: true });

// API endpoint to store simulated ride data
app.post('/api/ride', async (req, res) => {
  try {
    const rideData = simulatedRideData; // Get the simulated ride data generated earlier
    await RideDataModel.create(rideData); // Store the ride data in the database
    res.status(201).json({ message: 'Ride data stored successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred' });
  }
});

// API endpoint to store simulated delivery data
app.post('/api/delivery', async (req, res) => {
  try {
    const deliveryData = simulatedDeliveryData; // Get the simulated delivery data generated earlier
    await DeliveryDataModel.create(deliveryData); // Store the delivery data in the database
    res.status(201).json({ message: 'Delivery data stored successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred' });
  }
});

// Start the server
app.listen(3000, () => {
  console.log('Server running on port 3000');
});
