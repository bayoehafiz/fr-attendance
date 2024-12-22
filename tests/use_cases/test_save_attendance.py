import json
import os
import pytest
from unittest.mock import patch, mock_open
from src.use_cases.save_attendance import save_attendance, ATTENDANCE_FILE

@pytest.fixture
def mock_attendance_file():
    m = mock_open(read_data='{"attendance": []}')
    with patch("builtins.open", m) as mock_file:
        yield mock_file

def get_written_data(mock_file):
    data = ''.join(call.args[0] for call in mock_file().write.mock_calls)
    return json.loads(data)

def test_save_attendance_creates_new_file_if_not_exists(mock_attendance_file):
    with patch("os.path.exists", return_value=False):
        save_attendance("John Doe", "check-in")
        mock_attendance_file.assert_any_call(ATTENDANCE_FILE, 'r')
        assert mock_attendance_file().write.call_count > 0
        written_data = get_written_data(mock_attendance_file)
        assert any(record["name"] == "John Doe" for record in written_data["attendance"])
        assert written_data["attendance"][0]["action"] == "check-in"

def test_save_attendance_adds_record_to_existing_file(mock_attendance_file):
    with patch("os.path.exists", return_value=True):
        save_attendance("Jane Doe", "check-out")
        mock_attendance_file.assert_any_call(ATTENDANCE_FILE, 'r')
        written_data = get_written_data(mock_attendance_file)
        assert len(written_data["attendance"]) == 1
        assert written_data["attendance"][0]["name"] == "Jane Doe"
        assert written_data["attendance"][0]["action"] == "check-out"

def test_save_attendance_handles_json_decode_error():
    with patch("builtins.open", mock_open(read_data='invalid json')) as mock_file:
        save_attendance("John Doe", "check-in")
        mock_file.assert_any_call(ATTENDANCE_FILE, 'r')
        assert mock_file().write.call_count > 0
        written_data = get_written_data(mock_file)
        assert any(record["name"] == "John Doe" for record in written_data["attendance"])

def test_save_attendance_handles_timezone(mock_attendance_file):
    with patch("src.use_cases.save_attendance.datetime") as mock_datetime:
        mock_datetime.now.return_value.isoformat.return_value = "2023-10-10T10:10:10+07:00"
        save_attendance("John Doe", "check-in")
        written_data = get_written_data(mock_attendance_file)
        assert written_data["attendance"][0]["timestamp"] == "2023-10-10T10:10:10+07:00"
        assert written_data["attendance"][0]["action"] == "check-in"
        written_data = get_written_data(mock_attendance_file)

def test_save_attendance_handles_file_not_found_error():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            save_attendance("John Doe", "check-in")
