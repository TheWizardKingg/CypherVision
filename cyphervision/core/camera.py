import cv2
import numpy as np

image = cv2.imread("assets/input/image.jpg")
image_resized=cv2.resize(image,(1920,1080))
cv2.imshow("window",image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()