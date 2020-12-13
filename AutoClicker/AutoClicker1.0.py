from pyautogui import click, position
from time import sleep

while True:
    pos = position()
    click(pos)
    # sleep(#) if want a interval

# Problems 
# - in need of a hot key
# - the click speed is too slow
