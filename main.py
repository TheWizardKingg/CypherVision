import cv2
from cyphervision.core.camera import CameraManager
from models.gestureRecognition import GestureRecognizer

camera = CameraManager()
camera.open()
print(camera.Isopen)
print(camera.camera.isOpened())
gesture_recognizer = GestureRecognizer()

while True:

    success, original_frame = camera.giveMeTheFrame()
    if not success: 
        break

    processed_frame = cv2.flip(gesture_recognizer.processThis(original_frame), 1)
    

    cv2.imshow("window", processed_frame)
    if cv2.waitKey(1) == ord('q'):
        break

camera.close()
gesture_recognizer.close()
cv2.destroyAllWindows




