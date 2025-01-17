import pyautogui
import time

time.sleep(5)
position = pyautogui.position()
print(position)

pyautogui.click(x=10, y=20)
time.sleep(1)
pyautogui.click(position)