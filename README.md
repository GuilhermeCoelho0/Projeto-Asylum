# Projeto Asylum

Projeto experimental em Python e AutoHotkey para investigar automação de gameplay em *Batman: Arkham* no PS5, usando o PS Remote Play.

## Objetivo

Explorar uma forma de:

1. Ler entradas do DualSense conectado ao PC.
2. Enviar comandos ao jogo pelo PS Remote Play.
3. Em etapas futuras, capturar e analisar a imagem do jogo para tomar decisões automaticamente.

O projeto ainda está em fase de testes. Os scripts atuais investigam principalmente a comunicação entre o controle, o Windows e o Remote Play. Eles ainda não implementam um bot que reconhece o jogo ou joga sozinho.

## O que já foi testado

- O DualSense conectado ao PC conseguiu controlar o Batman através do PS Remote Play.
- Um teste com PyAutoGUI enviou as teclas `X` e `Y`, mas o jogo não respondeu. O Remote Play continuou funcionando.
- Foram criados scripts para detectar o DualSense com Pygame e observar botões e eixos.
- Também foram criados protótipos que tentam converter o botão X do DualSense em uma tecla do Windows.
- Um protótipo em AutoHotkey tenta localizar a janela do Remote Play e enviar teclas. A interação chegou a causar problemas com o aplicativo, por isso essa abordagem precisa de mais investigação.

Os scripts de leitura e conversão do DualSense estão no repositório como protótipos. O resultado deles pode depender do controle, do computador e do foco da janela; não há um resultado confirmado de que tenham enviado comandos aceitos pelo Batman.

## Estrutura sugerida

```text
Projeto-Asylum/
├── README.md
├── requirements.txt
├── python/
│   ├── input_test.py
│   ├── teste_dualsense.py
│   ├── mapear_dualsense.py
│   ├── teste_x_remoteplay.py
│   └── teste_input_windows.py
└── autohotkey/
    ├── Projeto_Asylum_v0.1.ahk
    └── Projeto_Asylum_v0.1.1.ahk
```

## Scripts Python

### `input_test.py`

Envia as teclas `X` e `Y` com PyAutoGUI depois de uma contagem regressiva. Foi usado para verificar se o Remote Play receberia entradas de teclado. No teste registrado, o Batman não respondeu.

### `teste_dualsense.py`

Usa Pygame para listar controles conectados e mostrar mudanças nos botões e nos eixos do controle. É um teste de leitura do controle, não de envio de comandos ao jogo.

### `mapear_dualsense.py`

Pede que o usuário pressione botões e gatilhos para identificar os índices que o Pygame detecta no DualSense. Os índices podem variar conforme o controle, o driver e a configuração do computador.

### `teste_x_remoteplay.py`

Tenta detectar o botão X do DualSense com Pygame e enviar a tecla Espaço com PyAutoGUI. Isso envia uma tecla do Windows; não equivale a enviar o botão X de um controle ao PS5.

### `teste_input_windows.py`

Tenta detectar o botão X do DualSense e enviar Espaço pela API `SendInput` do Windows. Esse script é específico para Windows e também envia uma tecla de teclado, não um comando nativo de controle.

## Scripts AutoHotkey

### `Projeto_Asylum_v0.1.ahk`

Protótipo com uma janela simples, botões manuais e uma sequência de teste. Tenta localizar o PS Remote Play e enviar teclas para sua janela usando `ControlSend`.

### `Projeto_Asylum_v0.1.1.ahk`

Protótipo menor que procura a janela do Remote Play e exibe informações sobre ela. Não envia comandos ao jogo.

Os scripts usam a sintaxe do AutoHotkey v1. Confira a versão instalada antes de executá-los.

## Requisitos

- Windows
- Python
- Pygame para os scripts que leem o DualSense
- PyAutoGUI para os testes que enviam teclas
- PS Remote Play e um PS5 configurados
- AutoHotkey v1 para executar os protótipos `.ahk`

Instale as bibliotecas Python necessárias com:

```bash
python -m pip install pygame pyautogui
```

Nem todo script usa as duas bibliotecas. Não foi registrada uma versão específica do Pygame para este projeto.

## Como executar

Abra o terminal na pasta do projeto e execute o script desejado, por exemplo:

```bash
python python/teste_dualsense.py
```

Para testar o envio de teclas:

```bash
python python/input_test.py
```

Antes dos testes com o jogo, abra o PS Remote Play e deixe o jogo em uma situação segura. Alguns scripts enviam entradas automaticamente ou ficam aguardando até serem encerrados com `Ctrl+C`.

## Limitações conhecidas

- Uma tecla enviada ao Windows não é necessariamente reconhecida pelo Remote Play como botão de controle.
- A leitura de um botão do DualSense não significa que o programa consiga pressionar esse botão virtualmente.
- Índices de botões e eixos podem variar entre dispositivos e configurações.
- O projeto ainda não possui captura de imagem, reconhecimento de HUD ou detecção de ataques implementados.
- Controle virtual e integração com clientes alternativos de Remote Play são possibilidades em investigação, não funcionalidades concluídas.

## Próximos passos

1. Executar os scripts de leitura do DualSense e registrar os índices observados no ambiente utilizado.
2. Documentar separadamente os resultados de cada teste de envio de entrada.
3. Investigar uma forma confiável de enviar comandos de controle ao Remote Play.
4. Escolher como capturar a imagem do jogo.
5. Implementar e testar um reconhecimento visual pequeno antes de tentar automatizar o gameplay.
6. Atualizar este README conforme os resultados forem confirmados.

## Segurança

Os scripts de teclado podem enviar entradas para a janela que estiver em foco. Feche outros aplicativos sensíveis antes de executar os testes e mantenha o jogo em uma situação segura.

Não coloque senhas, tokens ou dados da conta PlayStation neste repositório.

## Aviso

Este é um projeto experimental e independente. *Batman*, *Batman: Arkham*, PlayStation, PS5, DualSense e PS Remote Play pertencem aos seus respectivos proprietários. O projeto não é afiliado nem endossado por eles.
