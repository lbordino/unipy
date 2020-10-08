import cv2
import imutils
import numpy as np
import pytesseract

img = cv2.imread('lambo.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (600, 400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Edged', edged)
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None
cv2.imshow('Crop', img)
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print("Contorno Non trovato")
else:
    detected = 1
    print("Contorno Trovato")

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    new_image = cv2.bitwise_and(img, img, mask=mask)
    img = cv2.resize(img, (500, 300))
    cv2.imshow('Contorno sulla macchina', img)
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

    text = pytesseract.image_to_string(Cropped, config='--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789ABCDEFGHILKJMNOPQRSTUVZX Y')
    print("La targa è", text)

    Cropped = cv2.resize(Cropped, (400, 200))

    cv2.imshow('Croppata', Cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
