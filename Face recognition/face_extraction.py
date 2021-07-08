from mtcnn import MTCNN
import numpy as np
import cv2


def extract_face(filename, required_size=(224, 224)):

    pixels = cv2.imread(filename)

    detector = MTCNN()

    results = detector.detect_faces(pixels)
    if len(results) != 0:
        x1, y1, width, height = results[0]['box']
        x2, y2 = x1 + width, y1 + height

        face = pixels[y1:y2, x1:x2]

        face = face.astype(np.float32)
        return cv2.resize(face, required_size)

    return None
