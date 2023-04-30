from HandDetector import HandDetector
import cv2
import pyautogui
import time


handDetector = HandDetector(min_detection_confidence=0.7)
webcamFeed = cv2.VideoCapture(0)
start_init = False
number = -1


while True:
    status, image = webcamFeed.read()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count = 0

    if (len(handLandmarks) != 0):

        if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:  # Right Thumb
            count = count+1
        elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:  # Left Thumb
            count = count+1
        if handLandmarks[8][2] < handLandmarks[6][2]:  # Index finger
            count = count+1
        if handLandmarks[12][2] < handLandmarks[10][2]:  # Middle finger
            count = count+1
        if handLandmarks[16][2] < handLandmarks[14][2]:  # Ring finger
            count = count+1
        if handLandmarks[20][2] < handLandmarks[18][2]:  # Little finger
            count = count+1

    cv2.putText(image, str(count), (45, 375),
                cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
    cv2.imshow("Volume", image)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        webcamFeed.release()


    if (count == 1):
        pyautogui.press('left')
    elif (count == 2):
        pyautogui.press('right')
    elif (count == 3):
        pyautogui.press('up')
    elif (count == 4):
        pyautogui.press('down')
        
    if not (number == count):
        if not (start_init):
            start_time = time.time()
            start_init = True
        if (count == 5):
            pyautogui.press('space')
    number = count
    start_init = False
