import subprocess
import requests
import time
import os

api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
ff_api_key = os.environ.get('FF_API_KEY')


# Define the Docker build and run commands
docker_build_cmd = ["docker", "build", "-t", "flask-weather-app", "."]
docker_run_cmd = ["docker", "run", "--rm","-d", "-p", "5000:5000", "-e", "OPENWEATHERMAP_API_KEY=%s" % api_key, "-e", "FF_KEY=%s" % ff_api_key, "--name", "weather-app", "flask-weather-app"]

# Execute Docker build
print("Building Docker image...")
subprocess.run(docker_build_cmd, check=True)

# Execute Docker run
print("Running Docker container...")
subprocess.run(docker_run_cmd, check=True)

time.sleep(10)

# Send an HTTP request to the container
url = "http://localhost:5000/v1/temperature?city="  
cities = [
    "San Diego", "San Jose", "New York", "Los Angeles", "Chicago", "Miami",
    "Seattle", "Boston", "Denver", "Austin", "Atlanta", "Portland", "Phoenix",
    "New Orleans", "Nashville", "Minneapolis", "Detroit", "Las Vegas", "Philadelphia", "Salt Lake City"
]
units = ["imperial", "metric"]

print("")

for city in cities:
    for unit in units:
        response = requests.get(f"{url}{city}&units={unit}")
        # response.raise_for_status()
        data = response.json()
        temperature = data.get("temperature")
        if temperature is not None:
            print(f"{city}: {temperature}°{unit.capitalize()}", end=" | ")
    print()  # Move to the next line after each city's data

print("")


stop_container_cmd = ["docker", "stop", "weather-app"]
remove_image_cmd = ["docker", "rmi", "flask-weather-app"]



subprocess.run(stop_container_cmd)
subprocess.run(remove_image_cmd)
