import cv2


# img = cv2.imread('imeges/5acdc5.jpg')
img = cv2.imread('imeges/Hugo-Boss.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=1)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 5, 155), thickness=2)

cv2.imshow('Result', img)
cv2.waitKey(0)

