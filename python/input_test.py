import time
import pyautogui


print("================================")
print("      PROJETO ASYLUM v0.1")
print("       INPUT TEST")
print("================================")
print()
print("O programa vai começar em 5 segundos.")
print("Deixe o PS Remote Play aberto e conectado ao PS5.")
print()
print("IMPORTANTE:")
print("Deixe o Batman em uma situação segura.")
print()

time.sleep(5)

print("Enviando tecla...")
pyautogui.press("x")

time.sleep(2)

print("Enviando segunda tecla...")
pyautogui.press("y")

time.sleep(2)

print("Teste terminado.")