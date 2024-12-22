import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from src.use_cases.capture_image import capture_image, get_known_faces_data, process_frame
from src.entities.face import Face

class TestCaptureImage(unittest.TestCase):

    @patch('cv2.VideoCapture')
    @patch('cv2.imshow')
    @patch('cv2.waitKey', return_value=13)
    @patch('src.use_cases.capture_image.load_known_faces')
    @patch('src.use_cases.capture_image.process_frame')
    def test_capture_image(self, mock_process_frame, mock_load_known_faces, mock_waitKey, mock_imshow, mock_VideoCapture):
        mock_video_capture = MagicMock()
        mock_video_capture.isOpened.return_value = True
        mock_video_capture.read.return_value = (True, np.zeros((480, 640, 3), dtype=np.uint8))
        mock_VideoCapture.return_value = mock_video_capture

        mock_load_known_faces.return_value = []

        capture_image("clock-in")

        mock_VideoCapture.assert_called_once_with(0)
        mock_video_capture.isOpened.assert_called_once()
        mock_video_capture.read.assert_called()
        mock_imshow.assert_called()
        mock_waitKey.assert_called()
        mock_process_frame.assert_called()

    def test_get_known_faces_data(self):
        known_faces = [Face(name="John Doe", encoding=[0.1, 0.2, 0.3])]
        encodings, names = get_known_faces_data(known_faces)

        self.assertEqual(len(encodings), 1)
        self.assertEqual(len(names), 1)
        self.assertEqual(names[0], "John Doe")
        np.testing.assert_array_equal(encodings[0], np.array([0.1, 0.2, 0.3], dtype=np.float32))

    @patch('face_recognition.face_locations')
    @patch('face_recognition.face_encodings')
    @patch('face_recognition.compare_faces')
    @patch('src.use_cases.capture_image.save_attendance')
    def test_process_frame(self, mock_save_attendance, mock_compare_faces, mock_face_encodings, mock_face_locations):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        known_face_encodings = [np.array([0.1, 0.2, 0.3], dtype=np.float32)]
        known_face_names = ["John Doe"]

        mock_face_locations.return_value = [(0, 0, 0, 0)]
        mock_face_encodings.return_value = [np.array([0.1, 0.2, 0.3], dtype=np.float32)]
        mock_compare_faces.return_value = [True]

        process_frame(frame, known_face_encodings, known_face_names, "clock-in")

        mock_face_locations.assert_called_once()
        mock_face_encodings.assert_called_once()
        mock_compare_faces.assert_called_once()
        mock_save_attendance.assert_called_once_with("John Doe", "clock-in")

if __name__ == '__main__':
    unittest.main()