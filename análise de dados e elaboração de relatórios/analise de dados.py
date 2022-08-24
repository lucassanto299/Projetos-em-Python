from IPython.display import display
import pyautogui 
import pyperclip
import time 
import pandas as pd 
pyautogui.hotkey('ctrl', 't')
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=935, y=45, clicks=2)
# pyautogui.alert('Vai começar, aperte OK e não mexa em nada')
pyautogui.hotkey('ctrl', 't')
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)
# time.sleep(4)
# print(pyautogui.position03374348084
pyautogui.click(x=397, y=285, clicks= 2)
time.sleep(3)
pyautogui.click(x=417, y=400)
pyautogui.click(x=2341, y=177)
time.sleep(3)
pyautogui.click(x=2085, y=610)
time.sleep(3)
df = pd.read_excel(r'C:\Users\lucas\Vendas.xlsx')
time.sleep(5)
display(df)
faturamento = df['Valor Final' ].sum()
qtde_produtos = df['Quantidade'].sum()
pyautogui.hotkey('ctrl', 't')
pyautogui.write('mail.google.com')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=88, y=175)
time.sleep(5)
pyautogui.write('lucassanto96@gmail.com')
time.sleep(5)
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(5)
assunto = "Relatório de Vendas de Ontem"
# time.sleep(5)
pyperclip.copy(assunto)
# time.sleep(5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
pyautogui.press('tab')
# time.sleep(5)
texto = f"""
Prezados, bom dia!

O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos foi de: {qtde_produtos:,}
Abraço!
"""
pyperclip.copy(texto)
# time.sleep(3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(4)
pyautogui.hotkey('ctrl', 'enter')
# time.sleep(4)
# print(pyautogui.position())