import os
import pyautogui
from time import sleep
os.startfile('C:\\Users\\xihao\\Desktop\\哔哩哔哩漫画.lnk')
sleep(8)
pyautogui.click(31, 138)
# Point(x=31, y=138)
sleep(0.5)
pyautogui.click(528, 390)
# Point(x=528, y=390)
sleep(8)
os.system('TASKKILL /F /IM C:\\Users\\xihao\\Desktop\\哔哩哔哩漫画.lnk')

# I'm so sad, turned out that they had an auto sign in everytime the app opens...
# I didn't even need pyautogui...
# Program works perfectly though :) I can use this for later codes.
# date 1/21/2021
