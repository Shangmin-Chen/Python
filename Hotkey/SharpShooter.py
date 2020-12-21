from pynput import keyboard
from pyautogui import keyUp, keyDown
from time import sleep

def on_activate():
    keyDown("q")
    sleep(2)
    keyUp("q")
def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('f'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
