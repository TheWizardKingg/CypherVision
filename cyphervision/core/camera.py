import cv2
import numpy as np


class CameraManager:

    def __init__(self):
        self.Isopen=False
        self.camera=None
        self.resolution=(0, 0)
        self.FPS=0

    def open(self):
        self.camera=cv2.VideoCapture(0)
        if not self.camera.isOpened():
            return
        
        self.Isopen=True
        self.resolution=(int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.FPS=self.camera.get(cv2.CAP_PROP_FPS)

        while True:
            ret, frame = self.camera.read()

            if not ret:
                break

            cv2.imshow("window", frame)

            if cv2.waitKey(1) == ord('q'):
                break
        self.close()

    def close(self):
        if self.camera is not None:
            self.camera.release()
        cv2.destroyAllWindows()
        self.Isopen=False

Cam1=CameraManager()
Cam1.open()
