import cv2
from utils.constants import *

"""
Author: Zhenwei Jiang
Finished Time: 13-8-2023
Function: The detectors of face and eye.
Notice: You need to download deep learning models for these detectors.
"""


def get_res(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_detect = cv2.CascadeClassifier(FACE_DETECTOR)
    face = faces_detect.detectMultiScale(gray, 1.05, 3)
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    eye_cascade = cv2.CascadeClassifier(EYE_DETECTOR)
    eye = eye_cascade.detectMultiScale(gray, 1.2, 35)
    for (x, y, w, h) in eye:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # resized = cv2.resize(img, (int(img.shape[1] // 3), int(img.shape[0] // 3)))
    resized = img
    return resized