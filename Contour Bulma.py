import cv2

imgg = cv2.imread('bt/1.bmp')
# cv2.imshow('Orjinal resim', imgg)
imz = cv2.GaussianBlur(imgg, (0, 0), 1)
im = cv2.fastNlMeansDenoisingColored(imz, None, 10, 10, 7, 10)

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, 2, 1)
img = cv2.drawContours(im, contours, -1, (255, 0, 0), 4)
resized_image = cv2.resize(img, (500, 500))
cv2.imshow('Pencere', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
