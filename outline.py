import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')


# photo[10:50, 20:50] = 255, 5, 155
cv2.rectangle(photo, (100, 100), (200, 200), (255, 5, 155), thickness=1)
cv2.line(photo, (20, 50), (100, 20), (255, 1, 155), thickness=2)

cv2.putText(photo, '20 let', (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 5, 155), thickness=1)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
