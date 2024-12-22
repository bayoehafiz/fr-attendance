import cv2
import numpy as np
import face_recognition
from typing import List, Tuple
from src.use_cases.load_known_faces import load_known_faces
from src.use_cases.save_attendance import save_attendance
from src.entities.face import Face

def capture_image(action: str) -> None:
    """
    Captures an image using the webcam and processes it to recognize faces.
    Records attendance based on recognized faces.

    Args:
        action (str): The action to record (e.g., "clock-in" or "clock-out").
    """
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Camera could not be opened. Check camera permissions.")
        return

    known_faces = load_known_faces()
    known_face_encodings, known_face_names = get_known_faces_data(known_faces)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Frame could not be captured. Retrying...")
            continue

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) == 13:  # Enter key pressed
            process_frame(frame, known_face_encodings, known_face_names, action)
            break

    video_capture.release()
    cv2.destroyAllWindows()

def get_known_faces_data(known_faces: List[Face]) -> Tuple[List[np.ndarray], List[str]]:
    """
    Extracts encodings and names from known faces.

    Args:
        known_faces (List[Face]): List of known faces.

    Returns:
        Tuple[List[np.ndarray], List[str]]: List of face encodings and list of face names.
    """
    known_face_encodings = [np.asarray(face.encoding, dtype=np.float32).flatten() for face in known_faces]
    known_face_names = [face.name for face in known_faces]
    return known_face_encodings, known_face_names

def process_frame(frame: np.ndarray, known_face_encodings: List[np.ndarray], known_face_names: List[str], action: str) -> None:
    """
    Processes a single frame to detect and recognize faces.

    Args:
        frame (np.ndarray): The frame to process.
        known_face_encodings (List[np.ndarray]): List of known face encodings.
        known_face_names (List[str]): List of known face names.
        action (str): The action to record (e.g., "clock-in" or "clock-out").
    """
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            save_attendance(name, action)
            print(f"{action} recorded for {name}")
        else:
            print("Unknown face detected. Attendance not recorded.")