from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/v1/temperature')
def get_temperature():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is missing."}), 400

    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    if not api_key:
        return jsonify({"error": "OpenWeatherMap API key is missing."}), 500

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return jsonify({"city": city, "temperature": temperature})
    else:
        return jsonify({"error": "City not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
