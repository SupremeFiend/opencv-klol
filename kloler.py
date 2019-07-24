"""
kloler (an anti-chatspam tool) using OpenCV
If the top part of the chat window changes (i.e. a msg is sent by the next person), pyautogui will type 'k lol' and hit enter
Author : Pranay Venkatesh (SupremeFiend)
"""
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pyautogui as pg
import time

# Delay so that you can get to WhatsApp window
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

def klolify ():
    pg.press('k')
    pg.press(' ')
    pg.press('l')
    pg.press('o')
    pg.press('l')
    pg.press('enter')

ref_top_screen = ImageGrab.grab(bbox = (45, 180, 700, 280)) # Reference for top part of chat window
while (True):
    screen = ImageGrab.grab(bbox = (45, 220, 800, 640)) # large image screen (unused)
    curr_top_screen = ImageGrab.grab(bbox = (45, 180, 700, 280)) # Updated top part of chat window
    cv2.imshow('window', cv2.Canny(cv2.cvtColor(np.array(curr_top_screen), cv2.COLOR_BGR2GRAY), threshold1 = 200, threshold2 = 300))# Displays the required top part of the window for reference
    if curr_top_screen != ref_top_screen:
        ref_top_screen = curr_top_screen # Updating the reference
        klolify()
        time.sleep(4) # No matter what, at least 4 seconds will elapse before the next 'k lol'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    ref_top_screen = curr_top_screen  # Updating the reference
