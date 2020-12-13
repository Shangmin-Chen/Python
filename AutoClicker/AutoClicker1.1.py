#  has ability to hold mouse

from pyautogui import mouseDown, mouseUp, position, FAILSAFE
from time import sleep

#  PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen.
FAILSAFE = True
while True:
    sleep(3)
    pos = position()
    mouseDown(pos)
    sleep(35)
    mouseUp(pos)
    # sleep(#) if want a interval

# Problems
# - failsafe is temporary, in need of a hot key
