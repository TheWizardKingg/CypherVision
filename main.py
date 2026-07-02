import cv2
from cyphervision.core.camera import CameraManager
from models.gestureRecognition import GestureRecognizer
from models.gestureRecognition import DetectGestures

camera = CameraManager()
camera.open()
print(camera.Isopen)
print(camera.camera.isOpened())
gesture_recognizer = GestureRecognizer()
detector=DetectGestures()

while True:

    success, original_frame = camera.giveMeTheFrame()
    if not success: 
        break

    original_frame, fingers = gesture_recognizer.processThis(original_frame)

    processed_frame = cv2.flip(original_frame, 1)
    hand_sign=detector.detectThisGesture(fingers)
    print(hand_sign)
    

    cv2.imshow("window", processed_frame)
    if cv2.waitKey(1) == ord('q'):
        break

camera.close()
gesture_recognizer.close()
cv2.destroyAllWindows




