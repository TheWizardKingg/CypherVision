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
            if hand.landmark[tip_id].x > hand.landmark[tip_id - 2].x:
                return True
        else:
            for i in hand.landmark:
                if hand.landmark[tip_id].y < hand.landmark[tip_id-2].y:
                    return True

        

    def processThis(self, original_frame):
        rgb_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB)

        results=self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            fingers=[]
            for hand in results.multi_hand_landmarks:
                for i in range(1,6):
                    if self.isFingerUp(hand, 4*i):
                        fingers.append(4*i)
                
                print(fingers)
                fingers.clear()

                    
                self.drawer.draw_landmarks(original_frame, hand, self.mp_hands.HAND_CONNECTIONS)
        
        return original_frame
    
    def close(self):
        self.hands.close()
    



