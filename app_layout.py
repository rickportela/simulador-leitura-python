import PySimpleGUI as sg

# Definição do layout da interface: lista de listas, cada sublista é uma linha na janela
layout = [
    [sg.Text('Total de páginas do livro:'), sg.Input(key='total_paginas')],          # Linha 1: texto e campo para total de páginas
    [sg.Text('Quantas páginas você já leu:'), sg.Input(key='paginas_lidas')],       # Linha 2: texto e campo para páginas já lidas
    [sg.Text('Quantas páginas pretende ler por dia:'), sg.Input(key='paginas_por_dia')],  # Linha 3: texto e campo para páginas por dia
    [sg.Button('Calcular dias restantes')]                                            # Linha 4: botão para iniciar cálculo
]

# Criação da janela com título e layout definidos
window = sg.Window('Calculadora de leitura', layout)

# Loop de eventos da janela, para ler ações do usuário
while True:
    event, values = window.read()  # Espera por um evento (clique, digitação, fechar janela etc)
    if event == sg.WIN_CLOSED:     # Se o usuário fechar a janela, encerra o loop
        break

# Fecha a janela após sair do loop
window.close()
