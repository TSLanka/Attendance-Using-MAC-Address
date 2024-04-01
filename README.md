# Attendance Tracking System Using-MAC-Address

This is a simple Flask-based web application that tracks attendance of students based on their device connections.

## Project Overview

The project consists of a Flask web application (`app.py`) that allows users to view attendance details of students. It uses JSON files to store student data, device data, and attendance records.

## Features

- Loads student data from a JSON file (`students.json`).
- Simulates retrieving connected devices and saves device data to a JSON file (`devices.json`).
- Verifies attendance by matching connected devices with student MAC IDs.
- Saves attendance records to JSON files (`present.json` and `absent.json`).
- Displays attendance information on a web page (`index.html`) using Flask and Jinja2 templating.

## Project Structure

- `app.py`: The main Flask application file containing routes and functions to load student data, retrieve connected devices, verify attendance, and render templates.
- `students.json`: JSON file containing details of students including their names, roll numbers, and MAC IDs.
- `devices.json`: JSON file to store details of connected devices.
- `present.json`: JSON file to store details of present students including their names, roll numbers, MAC IDs, and connection times.
- `absent.json`: JSON file to store details of absent students.
- `templates/index.html`: HTML template to display attendance information.
- `static/style.css`: CSS file for styling the HTML template.

## Setup Instructions

1. Install Python 3.x if you haven't already.
2. Clone or download this repository to your local machine.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the web application at `http://localhost:5000` in your web browser.

## Usage

1. Ensure that `students.json` contains the necessary student details.
2. Access the web application using a web browser.
3. View the attendance information displayed on the home page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

