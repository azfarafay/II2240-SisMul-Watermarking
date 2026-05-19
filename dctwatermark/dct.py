import cv2
import numpy as np

def apply_dct(image_float):
    return cv2.dct(image_float)

def apply_idct(dct_matrix):
    return cv2.idct(dct_matrix)