import cv2  # OpenCV kütüphanesi içe aktarma
import numpy as np  # Python ile bilimsel hesaplamanın temel kütüphanesi olan NumPy'yi içe aktarma

resim = cv2.imread('bt/1.bmp')  # Resmin okunması
cv2.imshow("Original Resim", resim)  # Orjinal resmin gösterilmesi
floatResim = np.float32(resim)  # Görüntünün işaretsiz 8 bit'den 32 bit float'a dönüştürülmesi
kriter = (
    cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)  # Kriterlerin tanımlanması ( type, max_iter, epsilon )
# cv2.TERM_CRITERIA_EPS - Belirtilen doğruluk, epsilon, ulaşılınca algoritma tekrarlamasını durdurur.
# cv2.TERM_CRITERIA_MAX_ITER - Belirtilen yineleme sayısından sonra algoritmayı durdurur, max_iter.
# cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - İki koşuldan herhangi biri karşılaşıldığında yinelemeyi durdurur.
# max_iter - Maksimum yineleme sayısını belirten sayı. Biz 10 aldık
# epsilon - Gerekli doğruluk. Biz 1 olarak aldık
k = 50  # Kümelerin sayısı
ret, label, centers = cv2.kmeans(floatResim, k, None, kriter, 50, cv2.KMEANS_RANDOM_CENTERS)
# k meaans ın rastgele merkez yaklaşımı algoritmasında kullanılması
markez = np.uint8(centers)  # Görüntünün float'tan işaretsiz tamsayıya dönüştürülmesi
res = markez[label.flatten()]  # Label'in temizlenmesi
res2 = res.reshape(resim.shape)  # Resmin yeniden şekillendirilmesi
cv2.imshow("K Means", res2)
cv2.imwrite("K Means.jpg", res2)  # Resmin disk'e kaydedilmesi
meanshift = cv2.pyrMeanShiftFiltering(resim, sp=15, sr=16, maxLevel=1,
                                      termcrit=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 5, 3))
# Resme meanshift algoritmasının uygulanması
cv2.imshow("Meanshift Resmi", meanshift)
cv2.imwrite("Meanshift.jpg", meanshift)

gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)  # Resmin RGB'den GRAY (Gri) tona çevrilmesi
# Gürültü kaldırma
imggg = cv2.GaussianBlur(gray, (3, 3), 0)

laplacian = cv2.Laplacian(imggg, cv2.CV_64F)
cv2.imwrite('lap.jpg', laplacian)
resimx = cv2.imread('lap.jpg')
laplaciann = cv2.cvtColor(resimx, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(laplaciann, 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # görüntüyü iki boyutlu hale getirmek için eşik değer uygulaması
fg = cv2.erode(thresh, None, iterations=1)  # Görüntüyü aşındırma işlemi
bgt = cv2.dilate(thresh, None, iterations=1)  # Görüntüyü genişletme işlemi
ret, bg = cv2.threshold(bgt, 255, 10, 255)  # Eşik değerinin uygulanması
marker = cv2.add(fg, bg)  # Ön plan ve arka plan'ın eklenmasi
canny = cv2.Canny(marker, 210, 150)  # Canny kenar dedektörü uygulanması
new, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)  # Chain yaklaşımıyla kontur bulma
marker32 = np.int32(marker)  # işaretin float 32 bit'e çevrilmesi
cv2.watershed(resimx, marker32)  # Watershed algoritmasının uygulanması
m = cv2.convertScaleAbs(marker32)
ret, thresh = cv2.threshold(m, 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Resmin binary görüntüye dönüştürmek için görüntüye eşik uygulanması

thresh_inv = cv2.bitwise_not(thresh)
res = cv2.bitwise_and(resimx, resimx, mask=thresh)  # Görüntü maskesinin atıştırmasıyla Bitwise dönüşümü
res3 = cv2.bitwise_and(resimx, resimx, mask=thresh_inv)  # Görüntü maskesinin tersi ile Bitwise dönüşümü
res4 = cv2.addWeighted(res, 1, res3, 1, 0)  # Ağırlıklı ortalamasının alınması
final = cv2.drawContours(res4, contours, -1, (0, 0, 255),
                         1)  # Görüntüye kırmızı renk ve piksel genişliği 1 olan konturları çizilmesi
cv2.imshow("Watershed", final)
cv2.imwrite("Watershed.jpg", final)
cv2.waitKey()
