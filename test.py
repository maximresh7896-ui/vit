print("hello")
print("world")

import pyautogui
import time
time.sleep(5)
for x in range(0,50,10):
    pyautogui.dragTo(896, 712+x)
    time.sleep(0.1)
    pyautogui.dragTo(760, 442+x)
    time.sleep(0.1)
    pyautogui.dragTo(973, 470+x)
