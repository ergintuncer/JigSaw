import cv2
import numpy as np

# load the image
image = cv2.imread("parcayeni.jpg", 1)
# image = cv2.GaussianBlur(imgg, (0, 0), 1)
# red color boundaries (R,B and G)
upper = [1, 0, 20]
lower = [60, 40, 200]

# create NumPy arrays from the boundaries
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")

# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask=mask)

ret, thresh = cv2.threshold(mask, 40, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    # draw in blue the contours that were founded
    cv2.drawContours(output, contours, -1, 255, 3)
    # find the biggest area
    c = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(c)
    # draw the book contour (in green)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the images
cv2.imshow("Result", np.hstack([image, output]))

cv2.waitKey(0)
