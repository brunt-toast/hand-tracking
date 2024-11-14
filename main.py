print("Importing libraries...")
import cv2
import time
import os
import HandTrackingModule as htm
import speech_recognition as sr
from pynput.keyboard import Key, Controller
import threading

print("Declaring important variables...")
# create a keyboard controller (this is used to control media)
keyboard = Controller()

# declare some variables for the camera
wCam, hCam = 640, 480

# create and configure camera
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# create an instance of the hand detector
detector = htm.handDetector(detectionCon=0.8, trackCon=0.7) # I find that these work well for me; feel free to play around


def hand_tracking():

    print("Program is ready!")

    while True:

        # get the image from the camera
        success, img = cap.read()

        # hand tracking for the image
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        # run if a hand is detected
        if len(lmList) != 0:

            # declare some variables
            indexOpen = False
            middleOpen = False
            ringOpen = False
            pinkyOpen = False

            # some unused code for thumb position detection; if your thumbs are that versatile, feel free to enable
            """if lmList[4][2] < lmList[2][2]:
                thumbOpen = True
                print("THUMB")"""

            # test if the fingers are open (extended) or closed (curled up)
            if lmList[8][2] < lmList[6][2]:  # if point 8 (tip) is lower than point 6 (pip) in Y axis
                indexOpen = True
            if lmList[12][2] < lmList[10][2]:
                middleOpen = True
            if lmList[16][2] < lmList[14][2]:
                ringOpen = True
            if lmList[20][2] < lmList[18][2]:
                pinkyOpen = True

            # if certain positions are detected, run commands
            if (indexOpen and pinkyOpen) and not (middleOpen or ringOpen):
                print("COMMAND: LOCK")
                os.system("rundll32.exe user32.dll,LockWorkStation")
            if (middleOpen and middleOpen and pinkyOpen) and not (indexOpen):
                print("COMMAND: PLAY MUSIC")
                keyboard.press(Key.media_play_pause)
                keyboard.release(Key.media_play_pause)
                time.sleep(1)
            if (indexOpen) and not (middleOpen or ringOpen or pinkyOpen):
                print("COMMAND: REWIND")
                keyboard.press(Key.media_previous)
                keyboard.release(Key.media_previous)
                time.sleep(1)
            if (pinkyOpen) and not (indexOpen or middleOpen or ringOpen):
                print("COMMAND: SKIP")
                keyboard.press(Key.media_next)
                keyboard.release(Key.media_next)
                time.sleep(1)
            if (middleOpen) and not (indexOpen or ringOpen or pinkyOpen):
                quit(0)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


def speech_recognition():

    while True:
        r = sr.Recognizer()

        with sr.Microphone(4) as source:
            print("Speak now")

            audio = r.listen(source)


        try:
            query = r.recognize_google(audio, language="en-GB")

            if query == "":
                query="[none]"

            if "quit" in query:
                quit(0)
            if "lock" in query:  # all of these being "if" makes it so you can string them together, so you can, for exmaple, say "lock and quit"
                os.system("rundll32.exe user32.dll,LockWorkStation")

        except sr.UnknownValueError as e:
            print(f"speech_recognition.UnknownValueError: {e}")
            query = ""
        except sr.RequestError as e:
            print(f"speech_recognition.RequestError: {e}")
            query = ""
        except Exception as e:
            print(f"Other exception: {e}")
            query = ""



print("Starting to track...")
ht = threading.Thread(target=hand_tracking)
# vc = threading.Thread(target=speech_recognition)
ht.start()
# vc.start()
