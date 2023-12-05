# Real-Time Sensor Data Visualization with Flask and Plotly

This repository contains a Flask application demonstrating real-time sensor data visualization on a web interface using Flask and Plotly.

## Overview

This project showcases the implementation of a web application that displays real-time sensor data. It generates simulated sensor data and renders it as a dynamic Plotly line graph on a webpage.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_URL>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application locally in your web browser at `http://127.0.0.1:5000/`.

## Usage

Upon accessing the application in your browser, the webpage will continuously update to display the latest sensor data in real-time. The included Plotly graph will dynamically represent the sensor data changes.

## Customization

To customize or integrate real sensor data:

- Replace the mock data generation in `app.py` with actual sensor data reading code.
- Modify the HTML and JavaScript files (`index.html`) to enhance the webpage layout or improve graph visualization.
- Adjust update intervals in the JavaScript code (`index.html`) as required.

## Dependencies

- Flask
- Plotly

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was created to demonstrate the capabilities of real-time sensor data visualization using Flask and Plotly.
