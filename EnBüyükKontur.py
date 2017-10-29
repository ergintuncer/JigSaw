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
    areaArray = []
    im2, contours, hierarchy = cv2.findContours(renkAraligi, 1, 1)
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        areaArray.append(area)
    sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)  # first sort the array by area
    enBuyukKontur = sorteddata[0][1]  # find the nth largest contour [n-1][1], in this case 2
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
    x, y, w, h = cv2.boundingRect(enBuyukKontur)  # draw it
    print(x, y, w, h)
    yeniresim = resim[y:(y + h), x:(x + w)]

    resimHsvRenkKodu = cv2.cvtColor(yeniresim, cv2.COLOR_BGR2HSV)
    enDusukRenk = np.array([10, 10, 10], np.uint8)
    enBuyukRenk = np.array([255, 255, 255], np.uint8)
    renkAraligi = cv2.inRange(resimHsvRenkKodu, enDusukRenk, enBuyukRenk)
    areaArray = []
    im2, contours, hierarchy = cv2.findContours(renkAraligi, 1, 1)
    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        areaArray.append(area)
    sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)  # first sort the array by area
    enBuyukKontur = sorteddata[0][1]  # find the nth largest contour [n-1][1], in this case 2
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
    with open('kodlar/' + str(k + 1) + '.txt', 'w') as f:
        f.write(np.array2string(enBuyukKontur, separator=','))
    x, y, w, h = cv2.boundingRect(enBuyukKontur)  # draw it
    cv2.drawContours(yeniresim, enBuyukKontur, -1, (0, 0, 255), 6)  # cv2.rectangle(im, (x,y),(x+w,y+h),(0,255,0),6)
    cv2.imwrite('resimler/' + str(k + 1) + '.jpg', yeniresim)
    print(str(k + 1) + ' :Tamam')
