import cv2
import numpy as np

resimler = ['re/1.jpg', 're/2.jpg', 're/3.jpg', 're/4.jpg', 're/5.jpg', 're/6.jpg', 're/7.jpg', 're/8.jpg', 're/9.jpg',
            're/10.jpg', 're/11.jpg', 're/12.jpg', 're/13.jpg', 're/14.jpg', 're/15.jpg', 're/16.jpg', 're/17.jpg',
            're/18.jpg', 're/19.jpg', 're/20.jpg', 're/21.jpg']
for k in range(0, len(resimler)):
    resim = cv2.imread(resimler[k])
    resimHsvRenkKodu = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
    enDusukRenk = np.array([10, 10, 10], np.uint8)
    enBuyukRenk = np.array([255, 255, 255], np.uint8)
    renkAraligi = cv2.inRange(resimHsvRenkKodu, enDusukRenk, enBuyukRenk)
    alanlarinTutulduguDizi = []
    im2, contours, hierarchy = cv2.findContours(renkAraligi, 1, 1)
    for i, c in enumerate(contours):
        alan = cv2.contourArea(c)  # Alanı bul
        alanlarinTutulduguDizi.append(alan)  # Diziye ekle
    alanlarinSiralanmisHali = sorted(zip(alanlarinTutulduguDizi, contours), key=lambda x: x[0],
                                     reverse=True)  # alanlara göre dizinin sıralanamsı
    enBuyukKontur = alanlarinSiralanmisHali[0][1]  # enbüyük kontur alanını al [n-1][1]
    x, y, w, h = cv2.boundingRect(enBuyukKontur)  # konturun kapsadığı Xmax Xmin Ymax ve Ymin bilgilerinin bulunması
    print(x, y, w, h)
    yeniResim = resim[y:(y + h), x:(x + w)]  # kenarlarda bulunan fazlalıklar silinerek yeni bir resmin oluşturulması

    # Burdan sonra oluşturulan yeni resimde tekrardan kontur bilgilerinin bulunup tutarlılığı arttırmak amaçlanmakta.
    resimHsvRenkKodu = cv2.cvtColor(yeniResim, cv2.COLOR_BGR2HSV)
    enDusukRenk = np.array([10, 10, 10], np.uint8)
    enBuyukRenk = np.array([255, 255, 255], np.uint8)
    renkAraligi = cv2.inRange(resimHsvRenkKodu, enDusukRenk, enBuyukRenk)
    alanlarinTutulduguDizi = []
    im2, contours, hierarchy = cv2.findContours(renkAraligi, 1, 1)
    for i, c in enumerate(contours):
        alan = cv2.contourArea(c)
        alanlarinTutulduguDizi.append(alan)
    alanlarinSiralanmisHali = sorted(zip(alanlarinTutulduguDizi, contours), key=lambda x: x[0],
                                     reverse=True)  # alanlara göre dizinin sıralanamsı
    enBuyukKontur = alanlarinSiralanmisHali[0][1]  # enbüyük kontur alanını al [n-1][1]
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # Seçilen kontur bilgilerinin dosyaya kaydedilmesi
    with open('kodlar/' + str(k + 1) + '.txt', 'w') as f:
        f.write(np.array2string(enBuyukKontur, separator=','))
    cv2.drawContours(yeniResim, enBuyukKontur, -1, (0, 0, 255), 6)  # kenarların üzerine 6px çizgi çizilmesi
    cv2.imwrite('resimler/' + str(k + 1) + '.jpg', yeniResim)  # Resmin kaydedilmesi
    print(str(k + 1) + ' .Resim tamamlandı.')
