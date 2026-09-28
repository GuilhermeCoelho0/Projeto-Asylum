#NoEnv
#Persistent
#SingleInstance Force
#InstallKeybdHook
#InstallMouseHook
SetWorkingDir %A_ScriptDir%
SendMode Input
SetKeyDelay, 30, 30

; ============================================================
;                 PROJETO ASYLUM - v0.1
;             Remote Play Controller Test
; ============================================================
;
; Objetivo:
;   Testar comunicação:
;
;   PC -> AutoHotkey -> PS Remote Play -> PS5
;
; Antes de tentar fazer o Batman jogar sozinho,
; vamos confirmar que conseguimos enviar comandos.
;
; ============================================================


; ------------------------------------------------------------
; CONFIGURAÇÕES
; ------------------------------------------------------------

global RemotePlayID := ""
global Running := false

; Intervalo entre comandos durante o teste
global TestDelay := 1000


; ------------------------------------------------------------
; GUI
; ------------------------------------------------------------

Gui, Color, 202020
Gui, Font, s10 cFFFFFF, Segoe UI

Gui, Add, Text, x20 y15 w300, PROJETO ASYLUM v0.1
Gui, Add, Text, x20 y45 w300 vStatusText, Status: procurando Remote Play...

Gui, Add, Button, x20 y80 w120 h35 gFindRemotePlay, Conectar
Gui, Add, Button, x150 y80 w120 h35 gTestButtons, Testar

Gui, Add, Text, x20 y135 w300, Controles manuais:

Gui, Add, Button, x20 y165 w55 h35 gAttack, X
Gui, Add, Button, x85 y165 w55 h35 gCounter, TRI
Gui, Add, Button, x150 y165 w55 h35 gStun, O
Gui, Add, Button, x215 y165 w55 h35 gJump, QUAD

Gui, Add, Text, x20 y220 w350, F8 = conectar Remote Play
Gui, Add, Text, x20 y245 w350, F9 = teste automático
Gui, Add, Text, x20 y270 w350, F10 = parar
Gui, Add, Text, x20 y295 w350, ESC = fechar

Gui, Show, w350 h340, Projeto Asylum

; Tenta encontrar automaticamente
Gosub, FindRemotePlay

return


; ============================================================
; ENCONTRAR REMOTE PLAY
; ============================================================

FindRemotePlay:

    global RemotePlayID

    ; Procura pelo executável
    WinGet, RemotePlayList, List, ahk_exe RemotePlay.exe

    if (RemotePlayList = 0)
    {
        RemotePlayID := ""

        GuiControl,, StatusText, Status: Remote Play NAO encontrado

        return
    }

    ; Procura uma janela válida
    Loop, %RemotePlayList%
    {
        currentID := RemotePlayList%A_Index%

        WinGetTitle, currentTitle, ahk_id %currentID%

        if InStr(currentTitle, "PS Remote Play")
        {
            RemotePlayID := currentID
            break
        }
    }

    if (RemotePlayID = "")
    {
        GuiControl,, StatusText, Status: janela nao encontrada
        return
    }

    GuiControl,, StatusText, Status: Remote Play conectado

return


; ============================================================
; FUNÇÃO PRINCIPAL DE ENVIO
; ============================================================

SendButton(button)
{
    global RemotePlayID

    ; Se não temos ID, tenta localizar novamente
    if (RemotePlayID = "")
    {
        Gosub, FindRemotePlay
    }

    if (RemotePlayID = "")
    {
        MsgBox, 48, Projeto Asylum, Remote Play nao encontrado.
        return
    }

    ; Envia pressionamento
    ControlSend,, {%button% down}, ahk_id %RemotePlayID%

    Sleep, 80

    ; Libera botão
    ControlSend,, {%button% up}, ahk_id %RemotePlayID%
}


; ============================================================
; BOTÕES DO CONTROLE
; ============================================================

Attack:
    SendButton("x")
return


Counter:
    SendButton("y")
return


Stun:
    SendButton("o")
return


Jump:
    SendButton("a")
return


; ============================================================
; TESTE AUTOMÁTICO
; ============================================================

TestButtons:

    global Running

    if (RemotePlayID = "")
    {
        Gosub, FindRemotePlay
    }

    if (RemotePlayID = "")
    {
        MsgBox, 48, Projeto Asylum, Conecte o Remote Play primeiro.
        return
    }

    if (Running)
        return

    Running := true

    GuiControl,, StatusText, Status: TESTE EM EXECUCAO

    MsgBox, 64, Projeto Asylum, % "O teste vai enviar uma sequencia de comandos.`n`n" 
        . "Certifique-se de que o Batman esteja em uma situacao segura.`n`n"
        . "Clique OK para iniciar."

    ; --------------------------------------------------------
    ; ATAQUE
    ; --------------------------------------------------------

    if (!Running)
        return

    SendButton("x")
    Sleep, %TestDelay%


    ; --------------------------------------------------------
    ; TRIANGULO / CONTRA
    ; --------------------------------------------------------

    if (!Running)
        return

    SendButton("y")
    Sleep, %TestDelay%


    ; --------------------------------------------------------
    ; CIRCULO / ATORDOAR
    ; --------------------------------------------------------

    if (!Running)
        return

    SendButton("o")
    Sleep, %TestDelay%


    ; --------------------------------------------------------
    ; QUADRADO / GADGET
    ; --------------------------------------------------------

    if (!Running)
        return

    SendButton("a")
    Sleep, %TestDelay%


    Running := false

    GuiControl,, StatusText, Status: teste concluido

    MsgBox, 64, Projeto Asylum, Teste concluido.

return


; ============================================================
; PARAR
; ============================================================

StopScript:

    Running := false

    ; Garante que nenhum botão fique pressionado
    if (RemotePlayID != "")
    {
        ControlSend,, {x up}, ahk_id %RemotePlayID%
        ControlSend,, {y up}, ahk_id %RemotePlayID%
        ControlSend,, {o up}, ahk_id %RemotePlayID%
        ControlSend,, {a up}, ahk_id %RemotePlayID%
    }

    GuiControl,, StatusText, Status: parado

return


; ============================================================
; HOTKEYS
; ============================================================

F8::
    Gosub, FindRemotePlay
return


F9::
    Gosub, TestButtons
return


F10::
    Gosub, StopScript
return


Esc::
    Gosub, StopScript
    ExitApp
return


; ============================================================
; FECHAR
; ============================================================

GuiClose:
    Gosub, StopScript
    ExitApp
return