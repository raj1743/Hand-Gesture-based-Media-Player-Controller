# Hand-Gesture-based-Media-Player-Controller
A python program to control the Media Player like VLC media player with Internal or external camera feed.
# Overview
This Python program uses OpenCV to caputer the live feed using the inbuilt or external camera of the computer.
From the live feed it detects the hand using Mediapipe library.
There are total 3 ways of controlling the Media Player in the "Media Player Controller" Folder.
- Finger-Counter: It detects the hand using handDetector module and then count th fingers raised with the logic of 21 landmarks of hand and command the Media Player as below:-
  - 1 finger raised: Seek Backward
  - 2 finger raised: Seek Forward
  - 3 finger raised: Volume Up
  - 4 finger raised: Volume Down
  - 5 finger raised: Play/Pause
  
- Thumb-Detection: It detects the direction of thumb by calculating the angle between Thumb-tip and palm landmark. And according to the direction it commands the Media Player
  - UP: Volume Up
  - Down: Volume Down
  - Left: Seek Backward
  - Right: Seek Forward
  
- Hand-Movement: It detets the movement of hand. And Acoording to the direction of hand's movement it commands the Media Player.
  - UP: Volume Up
  - Down: Volume Down
  - Left: Seek Backward
  - Right: Seek Forward
  
# Requirments
- OpenCV
- Mediapipe
- PyAutoGUI
