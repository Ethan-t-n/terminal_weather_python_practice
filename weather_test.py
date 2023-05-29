import unittest
import config
from unittest.mock import patch
from weather import get_weather

class WeatherAppTestCase(unittest.TestCase):
    @patch("weather.requests.get")
    def test_get_weather_valid_city(self, mock_get):
        expected_result = "Weather: Clear sky, Temperature: 300.15 K, Humidity: 40%"
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            "weather": [{"description": "Clear sky"}],
            "main": {"temp": 300.15, "humidity": 40}
        }
        
        result = get_weather("London", config.weather_key)
        
        self.assertEqual(result, expected_result)
    
    @patch("weather.requests.get")
    def test_get_weather_invalid_city(self, mock_get):
        expected_result = "City not found."
        mock_response = mock_get.return_value
        mock_response.json.return_value = {"cod": "404"}
        
        result = get_weather("InvalidCity", config.weather_key)
        
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()