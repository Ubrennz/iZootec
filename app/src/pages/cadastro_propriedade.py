import flet as ft
from components import base as tb

def cadastroPropriedade(page: ft.Page):
    page.title = "Casdastro da Propriedade"

    tb.topBar(page)

    page.add(
        ft.Text(
            "Cadastro do Propriedade",
            size=40,
            color=ft.Colors.BLACK,            
        ),
        ft.Container(height=3),     
    )

    def button_clicked(e):
        try:
            t.value = f'''Textboxes values are:
            '{nome_propriedade.value}',
            '{nome_proprietario.value}', 
            '{endereco_propriedade.value}', 
            '{float(tamanho_propriedade_em_hectares.value)}', 
            '{int(numero_piquetes.value)}'
            '{int(numero_curais.value)}'
            '{int(qtde_funcionarios.value)}'
            '{'Sim' if possui_maquinas_sim.value else 'Não' if possui_maquinas_nao.value else 'Não informado'}
            '{quais_maquinas.value if possui_maquinas_sim else None}'.'''
        except ValueError:
            t.value = "Preencha todos os campos corretamente! (Atenção aos campos numéricos)"
        
        page.update()

    def checkbox_changed(e):
        if e.control == possui_maquinas_sim and possui_maquinas_sim.value:
            possui_maquinas_nao.value = False
        elif e.control == possui_maquinas_nao and possui_maquinas_nao.value:
            possui_maquinas_sim.value = False

        page.update()

    t = ft.Text()

    estilo_padrao = {
        "border_color": ft.Colors.GREY,
        "focused_border_color": ft.Colors.GREEN,
        "cursor_color": ft.Colors.GREEN,
        "border_radius": 8,        
        "bgcolor": ft.Colors.WHITE,
        "color": ft.Colors.BLACK,
        "text_style": ft.TextStyle(weight=ft.FontWeight.BOLD),     
    }

    nome_propriedade = ft.TextField(hint_text="Nome da Propriedade", **estilo_padrao)
    nome_proprietario = ft.TextField(hint_text="Nome do Proprietario", **estilo_padrao)
    endereco_propriedade = ft.TextField(hint_text="Endereço da Propriedade", **estilo_padrao)
    tamanho_propriedade_em_hectares = ft.TextField(hint_text="Tamanho da Propriedade em Hectares", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_piquetes = ft.TextField(hint_text="Número de Piquetes", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_curais = ft.TextField(hint_text="Número de Curais", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    qtde_funcionarios = ft.TextField(hint_text="Quantidade de Funcionários", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
        
    possui_maquinas_sim = ft.Checkbox(label="Sim", label_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD))
    possui_maquinas_nao = ft.Checkbox(label="Não", label_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD))
    possui_maquinas_sim.on_change = checkbox_changed
    possui_maquinas_nao.on_change = checkbox_changed

    possui_maquinas_container = ft.Container(
        content=ft.Column([
            ft.Text("Possui máquinas?", weight="bold", size=18),
            possui_maquinas_sim,
            possui_maquinas_nao,            
        ]),        
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=8,
        padding=10,        
    )

    if possui_maquinas_sim:
        quais_maquinas = ft.TextField(hint_text="Quais Maquinas?", **estilo_padrao)

    botao = ft.ElevatedButton(
        text="Cadastrar",
        on_click=button_clicked,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.GREEN,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20)
        ),
        height=50,
        width=100
    )
    
    page.add(
        ft.Column(
            controls=[
                nome_propriedade,
                nome_proprietario,
                endereco_propriedade,
                tamanho_propriedade_em_hectares,
                numero_piquetes,
                numero_curais,
                qtde_funcionarios,
                possui_maquinas_container,                
                botao,
                t
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )

    
