import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bt/1.bmp', 1)
# Gri Skala
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Gürültü kaldırma
img1 = cv2.GaussianBlur(gray, (0, 0), 1)

# laplace sobel islemleri
laplacian = cv2.Laplacian(img1, cv2.CV_64F)
np.savetxt("dizi.cvs", laplacian, delimiter=",")
edges = cv2.Canny(img1, 100, 200)

plt.subplot(121), plt.imshow(gray, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Canny Edge'), plt.xticks([]), plt.yticks([])

plt.show()
