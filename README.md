**DAY-1 :**

1. Made the project's structure folder
2. started git tracking
3. installed imp packages (numpy, open-cv{cv2} )
4. beginner cv2 code 
5. implemented the main cameraManager file to open camera, read frames, release camera

**DAY-2 :**

1. Implemented the basic CameraManager class
2. Tested the camera working by gray camera frames
3. completed the camera entry point, preparing to make the next model (gesture recognition)
4. i was less productive today

**DAY-3 :**

1. fixed bugs in cyphervision/core/camera.py {added new functions to interact with classess outside the scope of camera.py}
2. new file made {gestureRecognition.py} to recognize gestures from camera using mediapipe
3. made a new class GestureRecognizer to keep track of all the methods, integrate it with CameraManager class
4. fixed circle communication between camera.py, gestureRecognition.py and main.py to hand over input frames, process them and output the result
5. main.py contains the main app loop which controls the flow of Camera object and gesture objecta and prints the result 

