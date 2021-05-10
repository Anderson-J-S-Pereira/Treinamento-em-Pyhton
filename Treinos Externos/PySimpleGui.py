# Nesse treino irei utilizar da tabuada 2.0 que fiz anteriormente, só que dessa vez com interface gráfica.
from PySimpleGUI import PySimpleGUI as sg
# Layout
sg.theme('Reddit')
layout = [
    [sg.text('Qual valor?',sg.input())]
    [sg.text('Quantas vezes?', sg.input())]
]
# Janela
janela = sg.window('Calculadora', layout)
# Ler os Eventos
while true:
    eventos, valores = janela.read()
    if eventos == sg.window_closed:
