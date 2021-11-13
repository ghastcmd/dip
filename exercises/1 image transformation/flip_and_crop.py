import cv2

image = cv2.imread('cat.jpg')

cropped_image = image[:, :100]
flipped_image_lr = image[:, ::-1, :]
flipped_image_up = image[::-1, :, :]

cv2.imshow('cat image', image)
cv2.imshow('cropped image', cropped_image)
cv2.imshow('flipped cat image up', flipped_image_up)
cv2.imshow('flipped cat image lr', flipped_image_lr)

cv2.waitKey()