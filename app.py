from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

weather_cache = {}

def get_weather(city):
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    if not api_key:
        return None, "OpenWeatherMap API key is missing."

    # Check if the data is already in the cache
    if city in weather_cache:
        return weather_cache[city], None

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        # Cache the data for future use
        weather_cache[city] = temperature
        return temperature, None
    else:
        return None, "City not found."

@app.route('/v1/temperature')
def get_temperature():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is missing."}), 400

    temperature, error = get_weather(city)
    if error:
        return jsonify({"error": error}), 404 if error == "City not found." else 500

    return jsonify({"city": city, "temperature": temperature})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
