import ctypes
import time
import pygame
import sys

# ============================================================
# CONFIGURAÇÃO
# ============================================================

# Botão X do seu DualSense
BOTAO_X = 0

# Tecla que vamos enviar ao Windows
# VK_SPACE = barra de espaço
VK_SPACE = 0x20

# ============================================================
# API NATIVA DO WINDOWS
# ============================================================

user32 = ctypes.windll.user32

INPUT_KEYBOARD = 1

KEYEVENTF_KEYUP = 0x0002


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
    ]


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [
            ("ki", KEYBDINPUT),
        ]

    _anonymous_ = ("_input",)

    _fields_ = [
        ("type", ctypes.c_ulong),
        ("_input", _INPUT),
    ]


def enviar_tecla(vk):
    """
    Pressiona e solta uma tecla usando
    diretamente a API nativa SendInput do Windows.
    """

    extra = ctypes.c_ulong(0)

    # Pressionar
    entrada_down = INPUT(
        type=INPUT_KEYBOARD,
        ki=KEYBDINPUT(
            wVk=vk,
            wScan=0,
            dwFlags=0,
            time=0,
            dwExtraInfo=ctypes.pointer(extra),
        ),
    )

    # Soltar
    entrada_up = INPUT(
        type=INPUT_KEYBOARD,
        ki=KEYBDINPUT(
            wVk=vk,
            wScan=0,
            dwFlags=KEYEVENTF_KEYUP,
            time=0,
            dwExtraInfo=ctypes.pointer(extra),
        ),
    )

    user32.SendInput(
        1,
        ctypes.byref(entrada_down),
        ctypes.sizeof(INPUT),
    )

    time.sleep(0.05)

    user32.SendInput(
        1,
        ctypes.byref(entrada_up),
        ctypes.sizeof(INPUT),
    )


# ============================================================
# INICIALIZAÇÃO DO DUALSENSE
# ============================================================

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle encontrado.")
    sys.exit()

controle = pygame.joystick.Joystick(0)
controle.init()

print("=" * 50)
print(" TESTE WINDOWS SENDINPUT")
print("=" * 50)
print()
print(f"Controle: {controle.get_name()}")
print()
print("DualSense X  ->  Windows SendInput -> SPACE")
print()
print("1. Abra o PS Remote Play.")
print("2. Conecte-se ao PS5.")
print("3. Deixe o Remote Play em primeiro plano.")
print("4. Não clique em outra janela.")
print("5. Aperte X no DualSense.")
print()
print("Pressione CTRL+C para sair.")
print()
print("Aguardando...")
print()

x_anterior = False

try:

    while True:

        pygame.event.pump()

        x_atual = controle.get_button(BOTAO_X)

        # Detecta somente o momento em que X é pressionado
        if x_atual and not x_anterior:

            print("[DUALSENSE] X detectado")

            enviar_tecla(VK_SPACE)

            print("[WINDOWS] SendInput -> SPACE enviado")
            print()

        x_anterior = x_atual

        time.sleep(0.01)

except KeyboardInterrupt:

    print()
    print("Teste encerrado.")

finally:

    controle.quit()
    pygame.quit()