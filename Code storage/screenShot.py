import pyautogui

#region=(stat x axis, start y axis, search with, search height)
regionSquare = pyautogui.screenshot(region=(1000 ,400 ,100, 100))
#remember / not \
#C:/Users/Talyn/Documents/gimports/searchSpace.jpg
regionSquare.save(r'C:/Users/Talyn/Documents/gimports/my_screenshot.jpg')
print(regionSquare)
print('all is well')