import pyautogui
from time import sleep

# time until writer starts writing
sleep(5)

text = open("so done", "r")

for i in text:
    pyautogui.typewrite(i)
    sleep(0.2)

# open a text file and let the program write
