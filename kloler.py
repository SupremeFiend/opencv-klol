import numpy as np
from PIL import ImageGrab
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
    screen = ImageGrab.grab(bbox = (45, 220, 800, 640))
    curr_top_screen = ImageGrab.grab(bbox = (45, 180, 700, 280)) # Updated top part of chat window
    cv2.imshow('window', cv2.cvtColor(np.array(curr_top_screen), cv2.COLOR_BGR2GRAY))
    if curr_top_screen != ref_top_screen:
        klolify()
        ref_top_screen = curr_top_screen # Updating the reference
        time.sleep(10) # No matter what, at least 10 seconds will elapse before the next 'k lol'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    ref_top_screen = curr_top_screen  # Updating the reference
