import numpy

def load_known_faces():
    # Dummy implementation - replace with actual loading logic
    # Ensure each face encoding is a consistent numpy array
    return [
        (numpy.random.rand(128).astype(numpy.float32), "Person 1"),
        (numpy.random.rand(128).astype(numpy.float32), "Person 2"),
        # Add more known faces as needed, ensuring correct format
    ]

