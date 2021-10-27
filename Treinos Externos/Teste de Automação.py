# Recursos necessários para a importação:
import pyautogui

pyautogui.alert("A automação será realizada.")
pyautogui.PAUSE = 2.0
pyautogui.press('winleft')
pyautogui.PAUSE = 5.0
pyautogui.write('Opera GX')
pyautogui.PAUSE = 2.0
pyautogui.press('enter')
pyautogui.PAUSE = 5.0
pyautogui.write('https://www.youtube.com')
pyautogui.PAUSE = 1.0
pyautogui.press('enter')
pyautogui.PAUSE = 2.0
pyautogui.hotkey('winleft', 'd')
pyautogui.PAUSE = 1.0
pyautogui.moveTo(x=1323, y=742)
pyautogui.click(x=1323, y=742)
pyautogui.PAUSE = 5.0
pyautogui.alert("Automação finalizada.")


#Comando que mostra os nomes das letras do teclado na biblioteca PyAutoGui.
#print(pyautogui.KEYBOARD_KEYS)
