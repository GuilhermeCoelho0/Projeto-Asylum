import pygame
import sys
import time

pygame.init()
pygame.joystick.init()

quantidade = pygame.joystick.get_count()

if quantidade == 0:
    print("Nenhum controle foi detectado.")
    print("Conecte o DualSense via USB e execute novamente.")
    sys.exit()

print(f"Controles detectados: {quantidade}")

for i in range(quantidade):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

    print("\n==============================")
    print(f"Controle: {joystick.get_name()}")
    print(f"Índice: {i}")
    print(f"Botões: {joystick.get_numbuttons()}")
    print(f"Eixos: {joystick.get_numaxes()}")
    print(f"Hats/D-Pad: {joystick.get_numhats()}")
    print("==============================")

joystick = pygame.joystick.Joystick(0)

estado_botoes = [
    joystick.get_button(i)
    for i in range(joystick.get_numbuttons())
]

estado_eixos = [
    joystick.get_axis(i)
    for i in range(joystick.get_numaxes())
]

print("\nTeste iniciado.")
print("Aperte os botões do DualSense.")
print("Movimente os analógicos.")
print("Pressione CTRL+C para sair.\n")

try:
    while True:
        pygame.event.pump()

        # Detecta botões
        for i in range(joystick.get_numbuttons()):
            atual = joystick.get_button(i)

            if atual != estado_botoes[i]:
                if atual:
                    print(f"[BOTÃO] {i} pressionado")
                else:
                    print(f"[BOTÃO] {i} solto")

                estado_botoes[i] = atual

        # Detecta analógicos
        for i in range(joystick.get_numaxes()):
            atual = joystick.get_axis(i)

            if abs(atual - estado_eixos[i]) > 0.15:
                print(f"[EIXO {i}] {atual:.2f}")
                estado_eixos[i] = atual

        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nTeste encerrado.")

finally:
    joystick.quit()
    pygame.quit()