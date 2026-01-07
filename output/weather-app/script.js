// Mock weather data
const mockWeatherData = {
  location: "New York, NY",
  temperature: 72,
  condition: "Sunny",
  humidity: 65,
  windSpeed: 5
};

// Function to update the weather display
function updateWeatherDisplay(data) {
  const weatherDisplay = document.getElementById('weather-display');
  weatherDisplay.innerHTML = `
    <h2>${data.location}</h2>
    <p>Temperature: ${data.temperature}°F</p>
    <p>Condition: ${data.condition}</p>
    <p>Humidity: ${data.humidity}%</p>
    <p>Wind Speed: ${data.windSpeed} mph</p>
  `;
}

// Simulate fetching data (in a real app, this would be an API call)
setTimeout(() => {
  updateWeatherDisplay(mockWeatherData);
}, 1000);
