import cv2
import numpy as np

image = cv2.imread('cat.jpg')
height, width = image.shape[:2]

translation_matrix = np.array([
    [1, 0, -30],
    [0, 1,  20]
], dtype=np.float32)

image = cv2.warpAffine(
    src=image, M=translation_matrix, dsize=(width, height)
)

cv2.imshow('translated cat image', image)

cv2.waitKey()