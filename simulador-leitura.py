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
    if event == 'Calcular dias restantes':
        # Verificar se os campos não estão vazios
        if not values['total_paginas'] or not values['paginas_lidas'] or not values['paginas_por_dia']:
            sg.popup("Por favor, preencha todos os campos.")
            continue
        
        # Verificar se os valores são números inteiros e positivos
        if (not values['total_paginas'].isdigit() or
            not values['paginas_lidas'].isdigit() or
            not values['paginas_por_dia'].isdigit()):
            sg.popup("Por favor, digite números inteiros positivos.")
            continue
        
        total_paginas = int(values['total_paginas'])
        paginas_lidas = int(values['paginas_lidas'])
        paginas_por_dia = int(values['paginas_por_dia'])
        
        # Verificar se já leu mais do que o total
        if paginas_lidas > total_paginas:
            sg.popup("Você já leu mais páginas do que o total do livro! Verifique os dados.")
            continue
        
        # Se páginas por dia for 0, não dá para calcular
        if paginas_por_dia == 0:
            sg.popup("Número de páginas por dia deve ser maior que zero.")
            continue
        
        # Cálculo dos dias restantes
        paginas_restantes = total_paginas - paginas_lidas
        dias_restantes = (paginas_restantes + paginas_por_dia - 1) // paginas_por_dia  # divisão arredondando pra cima
        
        sg.popup(f"Faltam {dias_restantes} dias para terminar o livro lendo {paginas_por_dia} páginas por dia.")

# Fecha a janela após sair do loop
window.close()
