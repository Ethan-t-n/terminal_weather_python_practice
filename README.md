# Terminal Weather App

The Terminal Weather App is a simple Python application that retrieves weather information for a given city using the OpenWeatherMap API. It provides a text-based interface to display the current weather, temperature, and humidity.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Getting Started

1. Clone the repository or download the project files.

2. Install the required dependencies by running the following command:
  ```terminal
  pip3 install requests
  ```
  (please note that you need python3 in order to run this command)

3. Obtain an API key from OpenWeatherMap by signing up at [https://openweathermap.org](https://openweathermap.org). Copy the API key to use in the app.
  
  (IMPORTANT: please note that you may need to wait 30 minutes to an hour for an email to notfy you that you're API key has been activated in order for this application to work)

4. Create a new file called `config.py` in the project directory.

5. Open the `config.py` file and define a variable called `weather_key` with your OpenWeatherMap API key. Save the file.

   Example:
   ```python
   weather_key = "PUT_YOUR_API_KEY_HERE"
   ```
6. Run the app by executing the following command in the terminal:
  ```terminal
  python3 weather.py
  ```
7. Enter the name of the city for which you want to retrieve the weather information.

## Running Tests

The project includes unit tests to verify the functionality of the `get_weather` function. To run the tests, execute the following command in the terminal:
```terminal
python3 weather_test.py
```

## Project Structure

The project files are organized as follows:

- `weather.py`: The main script that retrieves and displays weather information.
- `weather_test.py`: Unit tests for the `get_weather` function.
- `README.md`: Project documentation.
