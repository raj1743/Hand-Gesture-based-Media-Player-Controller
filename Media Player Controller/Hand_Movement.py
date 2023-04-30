import cv2
import mediapipe as mp
import numpy as np
import pyautogui as key

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def detect_hand(image, hands):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        x_min = y_min = x_max = y_max = 0
        for landmark in hand_landmarks.landmark:
            x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
            if x < x_min:
                x_min = x
            if y < y_min:
                y_min = y
            if x > x_max:
                x_max = x
            if y > y_max:
                y_max = y
        return (x_min, y_min, x_max-x_min, y_max-y_min)
    else:
        return None

    
def get_centroid(bbox):
    x, y, w, h = bbox
    cx = int(x + w/2)
    cy = int(y + h/2)
    return (cx, cy)

def detect_movement(prev_center, current_center):
    dx = current_center[0] - prev_center[0]
    dy = current_center[1] - prev_center[1]
    distance = np.sqrt(dx**2 + dy**2)

    if distance < 10:
        return 'none'

    angle = np.arctan2(dy, dx) * 180 / np.pi

    if angle < -45 and angle >= -135:
        return 'up'
    elif angle >= 45 and angle < 135:
        return 'down'
    elif angle >= 135 or angle < -135:
        return 'left'
    else:
        return 'right'

hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

prev_center = None


while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()
            
    # Detect the hand in the frame
    bbox = detect_hand(frame, hands)

    # If a hand is detected, track its movement
    if bbox is not None:
        # Get the centroid of the hand
        current_center = get_centroid(bbox)
        
        # Draw the bounding box and centroid position of the hand
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, current_center, 5, (0, 0, 255), -1)

        # Detect the direction of movement
        if prev_center is not None and current_center is not None:
            direction = detect_movement(prev_center, current_center)

            # Draw the direction of movement
            if direction != 'none':
                cv2.putText(frame, direction, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if direction == 'up':
                key.press('up')
            elif direction == 'down':
                key.press('down')
            elif direction == 'left':
                key.press('right')
            elif direction == 'right':
                key.press('left')  
        # Update the previous centroid position
        prev_center = current_center
        
    # Display the frame
    cv2.imshow('frame', frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()