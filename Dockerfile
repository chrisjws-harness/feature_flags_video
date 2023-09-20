# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python packages
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port the application runs on
EXPOSE 5000

# Set environment variable for OpenWeatherMap API key
ENV OPENWEATHERMAP_API_KEY=YOUR_API_KEY

# Set environment variable for a future API key
ENV FF_KEY=YOUR_FUTURE_API_KEY

# Run the application
CMD ["python", "app.py"]
