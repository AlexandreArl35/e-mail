import pyautogui
import time
import pyperclip

# Abrir o e-mail

pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write("Email")
time.sleep(2.5)
pyautogui.hotkey("enter")
time.sleep(3)

# Novo e-mail

pyautogui.hotkey("ctrl", "n")
time.sleep(1)

# Destinatario

pyautogui.write("rochinha.lopes.35@gmail.com")
time.sleep(1)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")

# Assunto

pyperclip.copy("Informações de Faturamento.")
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# Corpo do e-mail

#pyautogui.click(x=718, y=274, clicks=1)
pyautogui.hotkey("tab")
time.sleep(2)

texto = """
Prezados, bom dia.

O faturamento de ontem foi de: faturamento
A quantidade de produtos foi de: quantidade

Abs.
xxxxxxxxxxxx """

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
time.sleep(1.5)

# Enviar

pyautogui.hotkey("ctrl", "enter")
time.sleep(1)

# Fechar

pyautogui.click(x=1347, y=12, clicks=1)

