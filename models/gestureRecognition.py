import cv2
import mediapipe as mp
import numpy as np
from pynput.keyboard import Controller

keyboard = Controller()

class GestureRecognizer:

    def __init__(self):
        self.mp_hands=mp.solutions.hands

        self.hands=self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer=mp.solutions.drawing_utils

    def isFingerUp(self, hand, tip_id):
        if tip_id==4:
            if hand.landmark[tip_id].x < hand.landmark[tip_id - 1].x:
                return True
            else: 
                return False
        else:
            if hand.landmark[tip_id].y < hand.landmark[tip_id-2].y:
                return True
            else: 
                return False
                
    def gesture_info(self, results, original_frame):
        fingers=[]
        for hand in results.multi_hand_landmarks:
            for i in range(1,6):
                fingers.append(self.isFingerUp(hand, 4*i))
            self.drawer.draw_landmarks(original_frame, hand, self.mp_hands.HAND_CONNECTIONS)
        return fingers



        

    def processThis(self, original_frame):
        rgb_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB)

        results=self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            finger_list=self.gesture_info(results, original_frame)
        else: 
            finger_list=None


        return original_frame, finger_list
    
    def close(self):
        self.hands.close()

class DetectGestures:

    def __init__(self):
        self.tip_ids = [4, 8, 12, 16, 20]

    def detectThisGesture(self, fingers):

        # fingers = [thumb, index, middle, ring, pinky]
        # True = finger up {finger is open}

        if fingers == [False, False, False, False, False]:
            return "FIST"

        elif fingers == [False, True, False, False, False]:
            return "POINT"

        elif fingers == [False, True, True, False, False]:
            return "VICTORY"

        elif fingers == [False, True, True, True, True]:
            return "OPEN PALM"

        elif fingers == [False, True, False, False, True]:
            return "ROCK"

        elif fingers == [True, False, False, False, True]:
            return "CALL ME"

        elif fingers == [True, True, True, True, True]:
            return "FIVE"

        else:
            return "UNKNOWN"
    




