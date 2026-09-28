#NoEnv
#SingleInstance Force
#Persistent

SetTitleMatchMode, 2

Gui, Color, 202020
Gui, Font, s10 cFFFFFF, Segoe UI

Gui, Add, Text, x20 y15 w350, PROJETO ASYLUM v0.1.1
Gui, Add, Text, x20 y50 w350 vStatus, Status: procurando Remote Play...
Gui, Add, Button, x20 y90 w120 h35 gFindRemotePlay, Procurar

Gui, Show, w400 h150, Projeto Asylum

return


FindRemotePlay:

    WinGet, RemotePlayList, List, ahk_exe RemotePlay.exe

    if (RemotePlayList = 0)
    {
        GuiControl,, Status, Status: Remote Play NAO encontrado
        return
    }

    found := false

    Loop, %RemotePlayList%
    {
        id := RemotePlayList%A_Index%

        WinGetTitle, title, ahk_id %id%

        if InStr(title, "PS Remote Play")
        {
            found := true

            GuiControl,, Status, Status: Remote Play encontrado!
            
            MsgBox, 64, Projeto Asylum, % "Remote Play encontrado.`n`n"
                . "ID da janela: " id "`n"
                . "Titulo: " title

            break
        }
    }

    if (!found)
    {
        GuiControl,, Status, Janela do Remote Play nao encontrada
    }

return


GuiClose:
ExitApp