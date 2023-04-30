import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0);
hands = mp.solutions.hands  
hands_mesh = hands.Hands(static_image_mode=True, min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils  

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    op = hands_mesh.process(rgb)
    if op.multi_hand_landmarks:
        for i in op.multi_hand_landmarks:
            draw.draw_landmarks(frame,i,hands.HAND_CONNECTIONS,landmark_drawing_spec=draw.DrawingSpec(color=(0,255,0),circle_radius=2))
        

    cv2.imshow("Hand Tracking",frame)
    if cv2.waitKey(1) == 27: #press esc to close
        cv2.destroyAllWindows()
        cap.release()
        