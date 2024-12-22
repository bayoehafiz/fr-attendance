import unittest
import numpy
from src.interfaces.load_known_faces import load_known_faces

class TestLoadKnownFaces(unittest.TestCase):

    def test_load_known_faces_returns_list(self):
        known_faces = load_known_faces()
        self.assertIsInstance(known_faces, list)

    def test_load_known_faces_elements_are_tuples(self):
        known_faces = load_known_faces()
        for face in known_faces:
            self.assertIsInstance(face, tuple)
            self.assertEqual(len(face), 2)

    def test_load_known_faces_encodings_are_numpy_arrays(self):
        known_faces = load_known_faces()
        for face in known_faces:
            encoding, name = face
            self.assertIsInstance(encoding, numpy.ndarray)
            self.assertEqual(encoding.shape, (128,))
            self.assertEqual(encoding.dtype, numpy.float32)

    def test_load_known_faces_names_are_strings(self):
        known_faces = load_known_faces()
        for face in known_faces:
            encoding, name = face
            self.assertIsInstance(name, str)

if __name__ == '__main__':
    unittest.main()