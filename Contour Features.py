import cv2
import numpy as np

imgh = cv2.imread('parca.jpg')
img = cv2.cvtColor(imgh, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)
np.savetxt("siyahkutu.cvs", thresh, delimiter=",")

im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
print(M)
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print('Cx: ', cx, ' Cy: ', cy)
area = cv2.contourArea(cnt)
print('Alan: ', area)
perimeter = cv2.arcLength(cnt, True)
print('Çevre: ', perimeter)
epsilon = 0.01 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
hull = cv2.convexHull(cnt)
k = cv2.isContourConvex(cnt)

x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
imgf = cv2.drawContours(imgh, hull, -1, (0, 0, 255), 10)
resized_image = cv2.resize(imgf, (500, 500))
cv2.imshow('imgf', im)
print('approx', approx)

print('k: ', k)
cv2.waitKey(0)
