import cv2
import numpy as np


photo = cv2.imread('imeges/IMG_8482.JPG')
img = np.zeros((photo.shape[:2]), dtype='uint8')
circle = cv2.circle(img.copy(), (2000, 2000), 200, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=circle)

cv2.imshow('Result', img)



cv2.waitKey(0)
