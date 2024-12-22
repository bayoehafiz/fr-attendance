import unittest
from src.entities.face import Face

class TestFace(unittest.TestCase):
    def setUp(self):
        self.name = "John Doe"
        self.encoding = [0.1, 0.2, 0.3, 0.4]
        self.face = Face(self.name, self.encoding)

    def test_face_initialization(self):
        self.assertEqual(self.face.name, self.name)
        self.assertEqual(self.face.encoding, self.encoding)

    def test_face_name(self):
        new_name = "Jane Doe"
        self.face.name = new_name
        self.assertEqual(self.face.name, new_name)

    def test_face_encoding(self):
        new_encoding = [0.5, 0.6, 0.7, 0.8]
        self.face.encoding = new_encoding
        self.assertEqual(self.face.encoding, new_encoding)

if __name__ == '__main__':
    unittest.main()