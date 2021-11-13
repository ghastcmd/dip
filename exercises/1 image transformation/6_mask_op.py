import cv2
import numpy as np

image = cv2.imread('cat.jpg')

mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.rectangle(mask, (20, 40), (100, 170), 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('masked image', masked)

cv2.waitKey()