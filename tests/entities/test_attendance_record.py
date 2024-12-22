import unittest
from datetime import datetime
from src.entities.attendance_record import AttendanceRecord

class TestAttendanceRecord(unittest.TestCase):
    def test_attendance_record_creation(self):
        name = "John Doe"
        timestamp = datetime.now()
        action = "check-in"
        attendance_record = AttendanceRecord(name, timestamp, action)
        
        self.assertEqual(attendance_record.name, name)
        self.assertEqual(attendance_record.timestamp, timestamp)
        self.assertEqual(attendance_record.action, action)

    def test_attendance_record_action_check_in(self):
        check_in_record = AttendanceRecord("Jane Doe", datetime.now(), "check-in")
        self.assertEqual(check_in_record.action, "check-in")

    def test_attendance_record_action_check_out(self):
        check_out_record = AttendanceRecord("Jane Doe", datetime.now(), "check-out")
        self.assertEqual(check_out_record.action, "check-out")

if __name__ == '__main__':
    unittest.main()