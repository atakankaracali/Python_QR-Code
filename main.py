import pyqrcode
import cv2

n_url = input("ENTER URL: ")
url = pyqrcode.create(n_url)
url.png('qr_code.png', scale=12)
image = cv2.imread("qr_code.png")
cv2.imshow("QR KOD",image)
cv2.waitKey (0)
cv2.destroyAllWindows ()