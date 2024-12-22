import json
from datetime import datetime
import pytz
from src.entities.attendance_record import AttendanceRecord

ATTENDANCE_FILE = "attendance.json"
TIMEZONE = pytz.timezone('Asia/Bangkok')  # UTC+7

def save_attendance(name: str, action: str):
    try:
        with open(ATTENDANCE_FILE, 'r') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {"attendance": []}

    current_time = datetime.now(TIMEZONE).isoformat()
    new_record = AttendanceRecord(name=name, timestamp=current_time, action=action)
    data["attendance"].append(new_record.__dict__)

    with open(ATTENDANCE_FILE, 'w') as file:
        json.dump(data, file, indent=4)