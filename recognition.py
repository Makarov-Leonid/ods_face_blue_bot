import os

import cv2
import matplotlib.pyplot as plt

from config import result_storage_path


def blur_image(detector, filepath, filename):
    image_name_new = "handled_image_" + filename
    pixels = plt.imread(filepath)
    results = detector.detect_faces(pixels)

    x1, y1, width, height = results[0]['box']
    x2, y2 = x1 + width, y1 + height

    pixels = cv2.imread(filepath, cv2.COLOR_BGR2RGB)

    pixels[y1:y2, x1:x2] = cv2.medianBlur(pixels[y1:y2, x1:x2], 35)

    cv2.imwrite(os.path.join(f"{result_storage_path}", f"{image_name_new}"), pixels)
    return image_name_new
