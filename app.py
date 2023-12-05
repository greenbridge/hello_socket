from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Function to simulate sensor reading (replace this with actual sensor code)
def read_sensor():
    while True:
        # Simulate sensor data (random value between 0 and 100)
        sensor_value = random.randint(0, 100)
        yield sensor_value
        time.sleep(1)  # Simulate sensor reading every second

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor_data')
def sensor_data():
    return jsonify({'value': next(read_sensor())})

@app.route('/plot')
def plot():
    # Create a simple Plotly line graph
    x_data = list(range(10))  # X-axis data (e.g., time or iterations)
    y_data = [random.randint(0, 100) for _ in range(10)]  # Random Y-axis data (replace this with actual sensor data)

    plot_data = [{
        'x': x_data,
        'y': y_data,
        'type': 'scatter',
        'mode': 'lines+markers',
        'name': 'Sensor Data'
    }]

    return jsonify(plot_data)

if __name__ == '__main__':
    app.run(debug=True)
