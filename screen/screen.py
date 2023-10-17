import pyautogui
import time

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'./screen.png')

time.sleep(5)