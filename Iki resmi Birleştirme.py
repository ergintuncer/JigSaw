import cv2
import numpy as np

# resimleri yükle
imgA = cv2.imread('orange.jpg')
imgB = cv2.imread('orange.jpg')
# piramit sayisi
levels = 5
# Gauss piramitini set et
gaussianPyramidA = [imgA.copy()]

for i in range(1, levels):
    gaussianPyramidA.append(cv2.pyrDown(gaussianPyramidA[i - 1]))

# Gauss piramitini set et
gaussianPyramidB = [imgB.copy()]

for i in range(1, levels):
    gaussianPyramidB.append(cv2.pyrDown(gaussianPyramidB[i - 1]))

# laplace piramitini set et
laplacianPyramidA = [gaussianPyramidA[-1]]

for i in range(levels - 1, 0, -1):
    laplacian = cv2.subtract(gaussianPyramidA[i - 1], cv2.pyrUp(gaussianPyramidA[i]))

laplacianPyramidA.append(laplacian)
# Laplace piramidini tersleyerek set et
laplacianPyramidB = [gaussianPyramidB[-1]]

for i in range(levels - 1, 0, -1):
    laplacian = cv2.subtract(gaussianPyramidB[i - 1], cv2.pyrUp(gaussianPyramidB[i]))

laplacianPyramidB.append(laplacian)

# Laplace uygula
laplacianPyramidComb = []
for laplacianA, laplacianB in zip(laplacianPyramidA, laplacianPyramidB):
    rows, cols, dpt = laplacianA.shape
laplacianComb = np.hstack((laplacianA[:, 0:cols / 2], laplacianB[:, cols / 2:]))
laplacianPyramidComb.append(laplacianComb)

imgComb = laplacianPyramidComb[0]
for i in range(1, levels):
    imgComb = cv2.add(cv2.pyrUp(imgComb), laplacianPyramidComb[i])

# Sonuçları gözle
cv2.imshow('image', imgComb)
cv2.imwrite('image.png', imgComb)
cv2.waitKey(0)
cv2.destroyAllWindows()
