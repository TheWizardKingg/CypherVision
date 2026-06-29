import cv2
class CameraManager:

    def __init__(self):       #This simply keeps track of all the biginning camera state's data
        self.Isopen = False
        self.camera = None
        self.source = 0
        self.resolution = (0, 0)
        self.FPS = 0

    def open(self):                  # This opens the camera
        self.camera = cv2.VideoCapture(self.source)

        if not self.camera.isOpened():
            return

        self.Isopen = True

        self.resolution = (
            int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )

        self.FPS = self.camera.get(cv2.CAP_PROP_FPS)

    def read_frame(self):                # this thing returns two things, first (ret) is a bool value, whether the given frame is valid or not
        ret, frame = self.camera.read()      # frame is the actual frame returned by the built-in read() function
        return ret, frame

    def close(self):               # This simply closes the camera, freeing up resources
        if self.camera is not None:
            self.camera.release()

        cv2.destroyAllWindows()          
        self.Isopen = False

    def start(self):       # just a method to automate the upper three necessary function
        self.open()
        while True:
            if not self.read_frame()[0]:       # basically the first thing returned by read_frame method (ret [boolean value])
                break
            cv2.imshow("window", cv2.cvtColor(self.read_frame()[1],cv2.COLOR_BGR2GRAY))      # second thing returned by read_frame (the actual frame)
            if cv2.waitKey(1)==ord('q'):        # waitKey(...x...), here, x is the time in miliseconds to wait before destroying cv2 windows {0->infinite time}
                break         # checks, whether after 1 milisecond of showing result, whether user enters a specific key (aka q) to delete all windows
        self.close()

cam1= CameraManager()       # making an object
cam1.start()       # starting the object's work
