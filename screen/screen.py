# pip install pyautogui
# pip install Pillow
# pip install pyscreeze

import pyautogui
import time
import datetime
import os

def fnScreen():
    myDate = datetime.datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(myDate):
        os.makedirs(myDate)

    myTime = datetime.datetime.now().strftime("%H-%M-%S")

    myScreenshot = pyautogui.screenshot()
    myFile = r'./' + myDate + '/' + myTime + '.png'
    print(myFile,flush=True)
    myScreenshot.save(myFile)

while True:
    fnScreen()
    time.sleep(5)