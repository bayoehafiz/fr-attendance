from datetime import datetime

class AttendanceRecord:
    def __init__(self, name: str, timestamp: datetime, action: str):
        self.name = name
        self.timestamp = timestamp
        self.action = action