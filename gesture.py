import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import sys

# Initialize Mediapipe and PyAutoGUI
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
pyautogui.FAILSAFE = False

# Screen size
screen_w, screen_h = pyautogui.size()

# Function to check if a finger is up
def is_finger_up(landmarks, tip_id, pip_id):
    return landmarks[tip_id].y < landmarks[pip_id].y

# Open webcam
cap = cv2.VideoCapture(0)

# Mediapipe hands detection
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.6) as hands:
    last_click_time = 0
    click_cooldown = 0.4  # seconds

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Flip image for mirror view
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                lm = hand_landmarks.landmark

                # Get index finger tip position
                ix, iy = int(lm[8].x * w), int(lm[8].y * h)
                cv2.circle(frame, (ix, iy), 10, (255, 0, 255), -1)

                # Map to screen
                screen_x = np.interp(lm[8].x, [0, 1], [0, screen_w])
                screen_y = np.interp(lm[8].y, [0, 1], [0, screen_h])
                pyautogui.moveTo(screen_x, screen_y)

                # Finger status
                fingers = {
                    "index": is_finger_up(lm, 8, 6),
                    "middle": is_finger_up(lm, 12, 10),
                    "ring": is_finger_up(lm, 16, 14),
                    "pinky": is_finger_up(lm, 20, 18)
                }

                # Check for closed fist (all fingers down)
                if not any(fingers.values()):
                    print("Fist detected – exiting program.")
                    cap.release()
                    cv2.destroyAllWindows()
                    sys.exit()

                current_time = time.time()

                # Gesture-based mouse clicks
                if fingers["index"] and not fingers["middle"] and current_time - last_click_time > click_cooldown:
                    pyautogui.rightClick()
                    print("Right click")
                    last_click_time = current_time

                elif fingers["index"] and not fingers["ring"] and current_time - last_click_time > click_cooldown:
                    pyautogui.click()
                    print("Left click / OK")
                    last_click_time = current_time

                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the result
        cv2.imshow("Virtual Mouse", frame)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit manually
            break

cap.release()
cv2.destroyAllWindows()
