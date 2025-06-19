import flet as ft
from components import base as tb

def cadastroPropriedade(page: ft.Page):
    page.title = "Casdastro da Propriedade"

    tb.topBar(page)

    page.scroll = ft.ScrollMode.ALWAYS
    page.update()

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
            sistema_criacao = (
                "Confinamento" if sistema_criacao_confinamento.value else
                "Semi-confinado" if sistema_criacao_semi_confinado.value else
                "Apasto" if sistema_criacao_apasto.value else
                "Não informado"
            )

            t.value = f'''Textboxes values are:
            '{nome_propriedade.value}',
            '{nome_proprietario.value}', 
            '{endereco_propriedade.value}', 
            '{float(tamanho_propriedade_em_hectares.value)}', 
            '{int(numero_piquetes.value)}'
            '{int(numero_curais.value)}'
            '{int(qtde_funcionarios.value)}'
            '{'Sim' if possui_maquinas_sim.value else 'Não' if possui_maquinas_nao.value else 'Não informado'}'
            '{quais_maquinas.value}'
            '{int(qtde_total_animais.value)}'
            '{raca_predominante.value}'
            '{sistema_criacao}'
            '{'Sim' if usa_racao_sim.value else 'Não' if usa_racao_nao.value else 'Não informado'}'.'''
        except ValueError:
            t.value = "Preencha todos os campos corretamente! (Atenção aos campos numéricos)"
        
        page.update()

    def checkbox_possui_maquinas(e):
        if e.control == possui_maquinas_sim and possui_maquinas_sim.value:
            possui_maquinas_nao.value = False
        elif e.control == possui_maquinas_nao and possui_maquinas_nao.value:
            possui_maquinas_sim.value = False

        page.update()

    def checkbox_sistema_criacao(e):
        if e.control == sistema_criacao_confinamento and sistema_criacao_confinamento.value:
            sistema_criacao_semi_confinado.value = False
            sistema_criacao_apasto.value = False
        elif e.control == sistema_criacao_semi_confinado and sistema_criacao_semi_confinado.value:
            sistema_criacao_confinamento.value = False
            sistema_criacao_apasto.value = False
        elif e.control == sistema_criacao_apasto and sistema_criacao_apasto.value:
            sistema_criacao_confinamento.value = False
            sistema_criacao_semi_confinado.value = False

        page.update()

    def checkbox_usa_racao(e):
        if e.control == usa_racao_sim and usa_racao_sim.value:
            usa_racao_nao.value = False
        elif e.control == usa_racao_nao and usa_racao_nao.value:
            usa_racao_sim.value = False

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

    estilo_label = {
        "label_style": ft.TextStyle(size=18, weight=ft.FontWeight.BOLD)
    }

    nome_propriedade = ft.TextField(hint_text="Nome da Propriedade", **estilo_padrao)
    nome_proprietario = ft.TextField(hint_text="Nome do Proprietario", **estilo_padrao)
    endereco_propriedade = ft.TextField(hint_text="Endereço da Propriedade", **estilo_padrao)
    tamanho_propriedade_em_hectares = ft.TextField(hint_text="Tamanho da Propriedade em Hectares", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_piquetes = ft.TextField(hint_text="Número de Piquetes", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_curais = ft.TextField(hint_text="Número de Curais", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    qtde_funcionarios = ft.TextField(hint_text="Quantidade de Funcionários", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
        
    possui_maquinas_sim = ft.Checkbox(label="Sim", **estilo_label)
    possui_maquinas_nao = ft.Checkbox(label="Não", **estilo_label)
    possui_maquinas_sim.on_change = checkbox_possui_maquinas
    possui_maquinas_nao.on_change = checkbox_possui_maquinas

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

    quais_maquinas = ft.TextField(hint_text="Quais maquinas?", **estilo_padrao)
    qtde_total_animais = ft.TextField(hint_text="Quantidade Total de Animais", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    raca_predominante = ft.TextField(hint_text="Raça Predominante", **estilo_padrao)

    sistema_criacao_confinamento = ft.Checkbox(label="Confinamento", **estilo_label)
    sistema_criacao_semi_confinado = ft.Checkbox(label="Semi-confinado", **estilo_label)
    sistema_criacao_apasto = ft.Checkbox(label="Apasto", **estilo_label)
    sistema_criacao_confinamento.on_change = checkbox_sistema_criacao
    sistema_criacao_semi_confinado.on_change = checkbox_sistema_criacao
    sistema_criacao_apasto.on_change = checkbox_sistema_criacao

    sistema_criacao_container = ft.Container(
        content=ft.Column([
            ft.Text("Sistema de Criacão", weight="bold", size=18),
            sistema_criacao_confinamento,
            sistema_criacao_semi_confinado,
            sistema_criacao_apasto,
        ]),        
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=8,
        padding=10,        
    )

    usa_racao_sim = ft.Checkbox(label="Sim", **estilo_label)
    usa_racao_nao = ft.Checkbox(label="Não", **estilo_label)
    usa_racao_sim.on_change = checkbox_usa_racao
    usa_racao_nao.on_change = checkbox_usa_racao

    usa_racao_container = ft.Container(
        content=ft.Column([
            ft.Text("Usa ração?", weight="bold", size=18),
            usa_racao_sim,
            usa_racao_nao,            
        ]),        
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=8,
        padding=10,        
    )

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
                quais_maquinas,
                qtde_total_animais,
                raca_predominante,
                sistema_criacao_container,
                usa_racao_container,                  
                botao,
                t
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15            
        )
    )    
