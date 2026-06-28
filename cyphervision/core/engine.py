from cyphervision.core.camera import CameraManager
import cv2

class Engine:
    def __init__(self):
        self.camera=CameraManager()
    
    def run(self):
        self.camera.open()
        while True:
            success, frame = self.camera.read_frame()
            if not success:
                break

            cv2.imshow("window",frame)
            if cv2.waitKey(1) == ord('q'):
                break

        self.camera.close()