"""Writing this program as a response to instagram bots in my direct messages"""
from pyautogui import typewrite, press
from time import sleep

sleep(5)    # give me time to set things up
names = open("Names", "r")

for i in names:
    text = (i.replace("\n", "") + ' said "nice bot bro"')
    typewrite(text)
    sleep(1)
    press("enter")

# Key take away:
# i.replace("\n", "") removes \n when text is in a multiple lines
