import cv2
import mediapipe as mp
import numpy as np

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


    def processThis(self, original_frame):
        rgb_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB)

        results=self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                self.drawer.draw_landmarks(original_frame, hand, self.mp_hands.HAND_CONNECTIONS)
        
        return original_frame
    
    def close(self):
        self.hands.close()
    



