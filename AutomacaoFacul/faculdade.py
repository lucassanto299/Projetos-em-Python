from os import link
from IPython.display import display
import pyautogui 
import pyperclip
import time 
import pandas as pd 
pyautogui.hotkey('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=491, y=37, clicks=2)
link = 'https://senac.blackboard.com/webapps/login/'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('enter')
time.sleep(4)
# time.sleep(5)
# print(pyautogui.position())
pyautogui.click(x=1276, y=593, clicks= 2)
time.sleep(2)
pyautogui.write('******')
time.sleep(2)
pyautogui.press('tab')
pyautogui.write('******')
time.sleep(2)
pyautogui.press('enter')
time.sleep(6)
pyautogui.click(x=220, y=813, clicks=2)   #Engenharia de software
time.sleep(6)
pyautogui.click(x=137, y=675, clicks=2)   #Web Conferencia
time.sleep(10)
pyautogui.click(x=332, y=441, clicks=2)   #Seleciona
time.sleep(5)
pyautogui.click(x=2207, y=427, clicks=1)  #Start
time.sleep(15)
pyautogui.click(x=2515, y=999, clicks=1)
time.sleep(2)
pyautogui.click(x=2368, y=906, clicks=2)
time.sleep(2)
pyautogui.write('Bom dia!')
time.sleep(2)
pyautogui.press('enter')
