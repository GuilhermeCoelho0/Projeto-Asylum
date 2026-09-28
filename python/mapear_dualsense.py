import pygame
import sys
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle encontrado.")
    sys.exit()

controle = pygame.joystick.Joystick(0)
controle.init()

print("Controle detectado:")
print(controle.get_name())
print()

# ---------------------------------------------------------
# Detectar botão normal
# ---------------------------------------------------------

def esperar_botao(nome):
    print(f"Aperte {nome}...")

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.JOYBUTTONDOWN:
                print(f"  -> {nome} = BOTÃO {evento.button}")
                return evento.button

        time.sleep(0.01)


# ---------------------------------------------------------
# Detectar gatilho
# ---------------------------------------------------------

def esperar_gatilho(nome, eixo):
    print(f"Aperte {nome}...")

    # Valor inicial do gatilho
    valor_inicial = controle.get_axis(eixo)

    while True:
        pygame.event.pump()

        valor = controle.get_axis(eixo)

        # O DualSense normalmente fica em -1 quando solto
        # e se aproxima de +1 quando pressionado.
        if valor > -0.50:

            print(
                f"  -> {nome} = EIXO {eixo} "
                f"(valor: {valor:.2f})"
            )

            # Espera soltar o gatilho antes de continuar
            while controle.get_axis(eixo) > -0.80:
                pygame.event.pump()
                time.sleep(0.01)

            return eixo

        time.sleep(0.01)


# ---------------------------------------------------------
# Mapeamento
# ---------------------------------------------------------

mapeamento_botoes = {}

botoes = [
    "X",
    "O",
    "QUADRADO",
    "TRIÂNGULO",
    "L1",
    "R1",
    "OPTIONS",
    "CREATE",
    "BOTÃO PS",
    "L3",
    "R3"
]

for nome in botoes:
    numero = esperar_botao(nome)
    mapeamento_botoes[nome] = numero
    print()


# ---------------------------------------------------------
# L2 e R2
# ---------------------------------------------------------

l2 = esperar_gatilho("L2", 4)
print()

r2 = esperar_gatilho("R2", 5)
print()


# ---------------------------------------------------------
# Resultado
# ---------------------------------------------------------

print()
print("=" * 45)
print("MAPEAMENTO DO SEU DUALSENSE")
print("=" * 45)

for nome, numero in mapeamento_botoes.items():
    print(f"{nome:12} -> BOTÃO {numero}")

print(f"{'L2':12} -> EIXO {l2}")
print(f"{'R2':12} -> EIXO {r2}")

print("=" * 45)

controle.quit()
pygame.quit()