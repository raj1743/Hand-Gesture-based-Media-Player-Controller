import cv2
import mediapipe as mp
import math
import pyautogui as key

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while True:
    ret, frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # get the landmark coordinates for the thumb and wrist
            thumb_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            wrist_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # calculate the angle between the thumb and wrist landmarks
            angle = math.atan2(thumb_landmark.y - wrist_landmark.y, thumb_landmark.x - wrist_landmark.x)
            angle = math.degrees(angle)
            if angle < 0:
                angle += 360

            # determine the direction of the thumb based on the angle
            if angle >= 45 and angle <= 135:
                direction = "down"
            elif angle >= 135 and angle <= 225:
                direction = "right"
            elif angle >= 225 and angle <= 315:
                direction = "up"
            else:
                direction = "left"
                
            

            # draw the direction text on the frame
            cv2.putText(frame, direction, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # draw a circle around the thumb landmark
            x = int(thumb_landmark.x * frame.shape[1])
            y = int(thumb_landmark.y * frame.shape[0])
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        if direction == 'up':
            key.press('up')
        elif direction == 'down':
            key.press('down')
        elif direction == 'left':
            key.press('right')
        elif direction == 'right':
            key.press('left')  
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
