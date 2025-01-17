import pyautogui
import time
import pandas

def click_reset(x=100, y=200):
  pyautogui.click(x=x,y=y)

pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')

pyautogui.press('enter')

time.sleep(1)
pyautogui.hotkey('win','up')

time.sleep(0.5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=712, y=373)
pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhaSenha')
pyautogui.press('tab')
pyautogui.press('enter')

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
  #print(tabela)
  click_reset()
  time.sleep(0.5)
  pyautogui.click(x=817, y=255)

  # codigo
  pyautogui.write(tabela.loc[linha, 'codigo'])
  pyautogui.press('tab')
  # marca
  pyautogui.write(tabela.loc[linha, 'marca'])
  pyautogui.press('tab')
  # Tipo
  pyautogui.write(tabela.loc[linha, 'tipo'])
  pyautogui.press('tab')
  # Categoria
  pyautogui.write(str(tabela.loc[linha, 'categoria']))
  pyautogui.press('tab')
  # preco unitario
  pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
  pyautogui.press('tab')
  # custo
  pyautogui.write(str(tabela.loc[linha, 'custo']))
  pyautogui.press('tab')
  # observacao
  obs =str(tabela.loc[linha, 'obs'])
  print(obs)
  if 'nan' != obs:
    pyautogui.write(obs)

  pyautogui.press('tab')

  # Enviar
  pyautogui.press('enter')

  pyautogui.scroll(10000)