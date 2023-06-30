// Simulated data generation for ride-hailing services
const generateRideData = () => {
    const rideData = [];
    for (let i = 0; i < 100; i++) {
      const ride = {
        id: i + 1,
        duration: Math.floor(Math.random() * 60) + 10, // Random duration between 10 and 70 minutes
        route: "Origin -> Destination",
        driverRating: Math.floor(Math.random() * 5) + 1, // Random driver rating between 1 and 5
        vehicleCondition: "Good",
        customerFeedback: "Satisfied",
      };
      rideData.push(ride);
    }
    return rideData;
  };
  
  // Simulated data generation for delivery companies
  const generateDeliveryData = () => {
    const deliveryData = [];
    for (let i = 0; i < 50; i++) {
      const delivery = {
        id: i + 1,
        duration: Math.floor(Math.random() * 120) + 30, // Random duration between 30 and 150 minutes
        route: "Origin -> Destination",
        deliveryAccuracy: "On time",
        customerFeedback: "Excellent",
      };
      deliveryData.push(delivery);
    }
    return deliveryData;
  };
  
  // Generate simulated ride-hailing data
  const simulatedRideData = generateRideData();
  
  // Generate simulated delivery data
  const simulatedDeliveryData = generateDeliveryData();
  