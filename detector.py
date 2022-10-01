import mtcnn


class neural_network:
    def __init__(self):
        self._detector = mtcnn.MTCNN()

    def detect_faces(self, pixels):
        return self._detector.detect_faces(pixels)
