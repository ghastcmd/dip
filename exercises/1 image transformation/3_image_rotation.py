import cv2

image = cv2.imread('cat.jpg')
height, width = image.shape[:2]
center = (width/2, height/2)

rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=54, scale=1)

image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

cv2.imshow('rotated image', image)
cv2.waitKey()