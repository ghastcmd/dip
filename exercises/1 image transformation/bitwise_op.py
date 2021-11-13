import cv2

image_cat = cv2.imread('cat.jpg')
image_dog = cv2.imread('dog.jpg')

height, width = image_cat.shape[:2]
image_dog = image_dog[:width, :height]

bit_or = cv2.bitwise_or(image_cat, image_dog)
bit_xor = cv2.bitwise_xor(image_cat, image_dog, mask=None)
bit_and = cv2.bitwise_and(image_cat, image_dog)

cv2.imshow('bitwise or', bit_or)
cv2.imshow('bitwise xor', bit_xor)
cv2.imshow('bitwise and', bit_and)

cv2.waitKey()