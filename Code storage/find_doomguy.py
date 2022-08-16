import pyautogui
import keyboard
import win32api, win32con
from time import sleep
#remember to use / not \
#C:/Users/Talyn/Documents/gimports/just_doomguy.jpg
#C:/Users/Talyn/Documents/gimports/just_demon.jpg
#C:/Users/Talyn/Documents/gimports/doomguyVSdemon-copy.jpg

#region=(stat x axis, start y axis, search with, search height)
#regionSquare = pyautogui.screenshot(region=(0 ,0 ,100, 100))

while 1:#why 1
    #confidence tetermins how close of a mach it must be
    if pyautogui.locateOnScreen('C:/Users/Talyn/Documents/gimports/just_doomguy.jpg', confidence=0.8) != None:
        print('I can see it')
        sleep(1)
    else:
        print('I am unable to see it')
        sleep(1)