import cv2

img1 = cv2.imread('bt/1.bmp', 0)
img2 = cv2.imread('bt/3.bmp', 0)
ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
img, contours1, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours1[0]
img1, contours, hierarchyy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]
n = len(contours) - 1
print(n)
x = 0.0

for i in range(0, n):
    x = float("{0:.4g}".format(x)) + float("{0:.4g}".format(cv2.matchShapes(contours1[i], contours[i], 1, 0.0)))
    print("{0:.4g}".format(x))

# ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
# print(cv2.matchShapes(contours1, contours, 1, 0.0))
