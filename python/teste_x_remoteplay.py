import pygame
import pyautogui
import time
import sys

# Inicializa o Pygame
pygame.init()
pygame.joystick.init()

# Verifica se existe um controle
if pygame.joystick.get_count() == 0:
    print("Nenhum DualSense encontrado.")
    sys.exit()

# Seleciona o primeiro controle
controle = pygame.joystick.Joystick(0)
controle.init()

print("========================================")
print(" TESTE DUALSENSE -> TECLADO")
print("========================================")
print()
print(f"Controle: {controle.get_name()}")
print()
print("X do DualSense  ->  ESPAÇO")
print()
print("IMPORTANTE:")
print("1. Deixe o PS Remote Play em primeiro plano.")
print("2. NÃO clique em outras janelas depois disso.")
print("3. Aperte X no DualSense.")
print("4. Pressione CTRL+C para encerrar.")
print()
print("Aguardando X...")
print()

# Botão X = botão 0
BOTAO_X = 0

# Evita enviar vários comandos enquanto X continua pressionado
x_anterior = False

try:

    while True:

        # Atualiza os eventos do controle
        pygame.event.pump()

        # Verifica X
        x_atual = controle.get_button(BOTAO_X)

        # Detecta apenas o momento em que X é pressionado
        if x_atual and not x_anterior:

            print("[X] Detectado!")

            # Envia ESPAÇO para o Windows
            pyautogui.press("space")

            print("[PYTHON] ESPAÇO enviado")

        x_anterior = x_atual

        time.sleep(0.01)

except KeyboardInterrupt:

    print()
    print("Teste encerrado pelo usuário.")

finally:

    controle.quit()
    pygame.quit()