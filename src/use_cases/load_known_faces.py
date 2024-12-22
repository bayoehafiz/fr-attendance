import os
import pickle
import face_recognition
from src.entities.face import Face

CACHE_FILE = 'known_faces_cache.pkl'
FACES_DIR = "faces/"

def load_known_faces():
    known_faces = []
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as file:
            known_faces = pickle.load(file)
        print("Loaded known faces from cache.")
    else:
        for image_name in os.listdir(FACES_DIR):
            image_path = os.path.join(FACES_DIR, image_name)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(Face(name=os.path.splitext(image_name)[0], encoding=encoding))

        with open(CACHE_FILE, 'wb') as file:
            pickle.dump(known_faces, file)
    return known_faces