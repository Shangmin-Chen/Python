from pynput import keyboard
from pyautogui import keyUp, keyDown
from time import sleep

COMBINATIONS = [
    {keyboard.KeyCode(char='q')}
]

current = set()

def execute():
    sleep(1)
    keyDown("e")
    sleep(2)
    keyUp("e")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
