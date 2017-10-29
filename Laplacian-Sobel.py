import cv2
from matplotlib import pyplot as plt

# loading image
img0 = cv2.imread('parca.jpg', )

# Gri Skala
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# Gürültü kaldırma
img = cv2.GaussianBlur(gray, (3, 3), 0)

# laplace sobel islemleri
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # x
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # y

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
