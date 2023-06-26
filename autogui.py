import pyautogui as pg
import time
from datetime import datetime
import random

# pyautogui.moveTo(100, 200, duration = 1)
# pyautogui.moveRel(0, 50, duration = 1)
# pyautogui.scroll(200)# makes program execution pause for 10 sec
# pyautogui.moveTo(1000, 1000, duration = 1)

# # moves mouse to 1000, 1000.
# pyautogui.dragRel(100, 0, duration = 1)

# # drags mouse 100, 0 relative to its previous position,
# # thus dragging it to 1100, 1000
# pyautogui.dragRel(0, 100, duration = 1)
# pyautogui.dragRel(-100, 0, duration = 1)
# pyautogui.dragRel(0, -100, duration = 1)

# pyautogui.typewrite("hello Geeks !")

# pg.click(100, 100)
# pg.typewrite("hello")
# time.sleep(1)


def fnShowCoords(i):
    print("pause {}".format(i))
    while (i > 0):
        # print(i, flush=True)
        print(pg.position(), flush=True)
        i -= 1
        time.sleep(1)


def fnClick(x, y, duration_):
    print(duration_, flush=True)
    pg.moveTo(x, y, duration=duration_)
    pg.click(x, y)


def fnScreen():
    # screen = pg.screenshot("/tmp/adsf.png")
    # screen = pg.screenshot()
    # fn = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # fn = "./"+fn+".png"
    # print(fn, flush=True)
    # screen.save(fn)
    pg.hotkey('ctrl', 'shift', 'p') 
    time.sleep(1)
    pg.typewrite('full size screen') 
    time.sleep(1)
    pg.hotkey('enter') 
    time.sleep(1)

def fnWhile():
    while True:
        fnClick(160, 80, 3)  # refresh
        # fnClick(1855, 115, 2)  # 3 dots 

        fnScreen()

        time.sleep(random.randrange(1, 10) * 60)


#########################################
print("start", flush=True)

print(pg.size())

fnShowCoords(5)

fnWhile()

print("stop")
