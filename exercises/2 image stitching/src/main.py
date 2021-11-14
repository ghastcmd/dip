import numpy as np
import cv2

images = [
    cv2.imread('images/ic1.jpg'),
    cv2.imread('images/ic2.jpg'),
    cv2.imread('images/ic3.jpg'),
    cv2.imread('images/ic4.jpg')
]
print('Loaded images')

# for i, image in enumerate(images):
#     cv2.imshow('ic' + str(i), image)
# cv2.waitKey()

print('Stitching images')
image_sticher = cv2.Stitcher_create()
error, stitched_image = image_sticher.stitch(images)
print('Completed stitching')

if not error:
    print('Saving output image')
    cv2.imwrite('images/ic.png', stitched_image)
    # cv2.imshow('Stitched image', stitched_image)
    # cv2.waitKey()
print('Exit...')