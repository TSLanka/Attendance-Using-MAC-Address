import json
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

class Student:
    def __init__(self, name, roll_number, mac_id):
        self.name = name
        self.roll_number = roll_number
        self.mac_id = mac_id

    def to_dict(self):
        return {
            'name': self.name,
            'roll_number': self.roll_number,
            'mac_id': self.mac_id
        }

def load_students(filename):
    print("Step 1: Loading student details...")
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            student_data = data.get("students", [])
            students = [Student(student['name'], student['roll_number'], student['mac_id']) for student in student_data]
        print("Student details loaded successfully")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print("Error loading student details:", e)
        return None

def get_connected_devices():
    print("Step 1: Getting connected devices...")
    # Add your code to retrieve connected devices here
    connected_devices = ['6c:03:b5:94:9f:f2']  # Dummy data for demonstration
    print("Connected devices retrieved")
    save_device_details(connected_devices)
    return connected_devices

def save_device_details(devices):
    print("Step 2: Saving device details...")
    try:
        with open('devices.json', 'w') as f:
            json.dump(devices, f)
        print("Device details saved to 'devices.json'")
    except Exception as e:
        print("Error saving device details:", e)

def verify_attendance(students, devices):
    print("Step 3: Verifying attendance...")
    if students is None:
        print("Cannot verify attendance. Student details not loaded.")
        return
    
    present_students = []
    absent_students = []
    
    for student in students:
        if student.mac_id in devices:
            connection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            student_info = {
                'name': student.name,
                'roll_number': student.roll_number,
                'mac_id': student.mac_id,
                'connection_time': connection_time
            }
            present_students.append(student_info)
        else:
            absent_students.append(student)
                
    with open('present.json', 'w') as f:
        json.dump(present_students, f, default=str)
    print("Present students saved to 'present.json'")
    
    with open('absent.json', 'w') as f:
        json.dump([s.__dict__ for s in absent_students], f, default=str)
    print("Absent students saved to 'absent.json'")

@app.route('/')
def index():
    students = load_students('students.json')
    connected_devices = get_connected_devices()
    
    if students is not None and connected_devices is not None:
        verify_attendance(students, connected_devices)
    else:
        print("Cannot verify attendance. Some data is missing.")
    
    with open('present.json', 'r') as f:
        present_data = json.load(f)
    with open('absent.json', 'r') as f:
        absent_data = json.load(f)

    return render_template('index.html', present_data=present_data, absent_data=absent_data)

if __name__ == '__main__':
    app.run(debug=True)
