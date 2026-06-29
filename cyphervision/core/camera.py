import cv2
class CameraManager:

    def __init__(self):
        self.Isopen = False
        self.camera = None
        self.source = 0
        self.resolution = (0, 0)
        self.FPS = 0

    def open(self):
        self.camera = cv2.VideoCapture(self.source)

        if not self.camera.isOpened():
            return

        self.Isopen = True

        self.resolution = (
            int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )

        self.FPS = self.camera.get(cv2.CAP_PROP_FPS)

    def read_frame(self):
        ret, frame = self.camera.read()
        return ret, frame

    def close(self):
        if self.camera is not None:
            self.camera.release()

        cv2.destroyAllWindows()
        self.Isopen = False

    def start(self):
        self.open()
        while True:
            if not self.read_frame()[0]: 
                break
            cv2.imshow("window", cv2.cvtColor(self.read_frame()[1],cv2.COLOR_BGR2GRAY))
            if cv2.waitKey(1)==ord('q'):
                break
        self.close()

cam1= CameraManager()
cam1.start()
