import pyautogui
import time
#pyautogui.press('win')

pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('https://web.marqponto.com.br/login')
pyautogui.press('enter')

time.sleep(5)
pyautogui.click(x=1081, y=413)
pyautogui.write('MILLENA@GMAIL.COM')

pyautogui.click(x=1101, y=469)
pyautogui.write('12345')