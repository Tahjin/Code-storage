import pyautogui
import random
import keyboard
import win32api, win32con
from time import sleep
#have magic piano tiles on half screen to the right kizi.com
#https://kizi.com/games/magic-piano-tiles
#theres nothing wrong with code just keep doing it
#title1  X:  919 Y:  440 RGB: (153, 159, 229)
#title2  X: 1031 Y:  440 RGB: (163, 169, 232)
#title3  X: 1125 Y:  440 RGB: (153, 159, 228)
#title4  X: 1224 Y:  440 RGB: (  0,   0,   0)
#
#RGB is color

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(919, 420)[0] == 0:
        click(919,420)
    if pyautogui.pixel(1031, 420)[0] == 0:
        click(1031,420)
    if pyautogui.pixel(1125, 420)[0] == 0:
        click(1125,420)
    if pyautogui.pixel(1224, 420)[0] == 0:
        click(1224,420)