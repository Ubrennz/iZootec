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
            '{nome_propriedade.value}'
            '{nome_proprietario.value}'
            '{endereco_propriedade.value}'
            {float(tamanho_propriedade_em_hectares.value)}
            {int(numero_piquetes.value)}
            {int(numero_curais.value)}
            {int(qtde_funcionarios.value)}
            '{'Sim' if possui_maquinas_sim.value else 'Não' if possui_maquinas_nao.value else 'Não informado'}'
            '{quais_maquinas.value}'
            {int(qtde_total_animais.value)}
            '{raca_predominante.value}'
            '{sistema_criacao}'
            '{'Sim' if usa_racao_sim.value else 'Não' if usa_racao_nao.value else 'Não informado'}
            '{'Concentrado' if tipo_alimentacao_concentrado.value else 'Volumoso' if tipo_alimentacao_volumoso else 'Não informado'}'.'''
        except ValueError:
            t.value = "Preencha todos os campos corretamente! (Atenção aos campos numéricos)"
        
        page.update()

    def checkbox(e, lista_checkbox):
        for checkbox in lista_checkbox:
            if checkbox != e.control:
                checkbox.value = False

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

    estilo_container = {
        "bgcolor": ft.Colors.WHITE,
        "border":ft.border.all(1, ft.Colors.GREY),
        "border_radius": 8,
        "padding": 10        
    }

    estilo_content = {
        "weight": ft.FontWeight.BOLD,
        "size": 18
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
    possui_maquinas_sim.on_change = lambda e: checkbox(e, [possui_maquinas_sim, possui_maquinas_nao])
    possui_maquinas_nao.on_change = lambda e: checkbox(e, [possui_maquinas_sim, possui_maquinas_nao])

    quais_maquinas = ft.TextField(hint_text="Se sim, quais maquinas?", border=ft.InputBorder.UNDERLINE, **estilo_padrao)
    
    possui_maquinas_container = ft.Container(
        content=ft.Column([
            ft.Text("Possui máquinas?", **estilo_content),
            possui_maquinas_sim,
            possui_maquinas_nao,
            quais_maquinas,
        ]),        
        **estilo_container        
    )
    
    qtde_total_animais = ft.TextField(hint_text="Quantidade Total de Animais", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    raca_predominante = ft.TextField(hint_text="Raça Predominante", **estilo_padrao)

    sistema_criacao_confinamento = ft.Checkbox(label="Confinamento", **estilo_label)
    sistema_criacao_semi_confinado = ft.Checkbox(label="Semi-confinado", **estilo_label)
    sistema_criacao_apasto = ft.Checkbox(label="Apasto", **estilo_label)
    sistema_criacao_confinamento.on_change = lambda e: checkbox(e, [sistema_criacao_confinamento, sistema_criacao_semi_confinado, sistema_criacao_apasto])
    sistema_criacao_semi_confinado.on_change = lambda e: checkbox(e, [sistema_criacao_confinamento, sistema_criacao_semi_confinado, sistema_criacao_apasto])
    sistema_criacao_apasto.on_change = lambda e: checkbox(e, [sistema_criacao_confinamento, sistema_criacao_semi_confinado, sistema_criacao_apasto])

    sistema_criacao_container = ft.Container(
        content=ft.Column([
            ft.Text("Sistema de Criacão", **estilo_content),
            sistema_criacao_confinamento,
            sistema_criacao_semi_confinado,
            sistema_criacao_apasto,
        ]),        
        **estilo_container        
    )

    usa_racao_sim = ft.Checkbox(label="Sim", **estilo_label)
    usa_racao_nao = ft.Checkbox(label="Não", **estilo_label)
    usa_racao_sim.on_change = lambda e: checkbox(e, [usa_racao_sim, usa_racao_nao])
    usa_racao_nao.on_change = lambda e: checkbox(e, [usa_racao_sim, usa_racao_nao])

    usa_racao_container = ft.Container(
        content=ft.Column([
            ft.Text("Usa ração?", **estilo_content),
            usa_racao_sim,
            usa_racao_nao,            
        ]),        
        **estilo_container       
    )

    tipo_alimentacao_concentrado = ft.Checkbox(label="Concentrado", **estilo_label)
    tipo_alimentacao_volumoso = ft.Checkbox(label="Volumoso", **estilo_label)
    tipo_alimentacao_concentrado.on_change = lambda e: checkbox(e, [tipo_alimentacao_concentrado, tipo_alimentacao_volumoso])
    tipo_alimentacao_volumoso.on_change = lambda e: checkbox(e, [tipo_alimentacao_concentrado, tipo_alimentacao_volumoso])

    fornece_sal_mineral_sim = ft.Checkbox(label="Sim", **estilo_label)
    fornece_sal_mineral_nao = ft.Checkbox(label="Não", **estilo_label)
    fornece_sal_mineral_sim.on_change = lambda e: checkbox(e, [fornece_sal_mineral_sim, fornece_sal_mineral_nao])
    fornece_sal_mineral_nao.on_change = lambda e: checkbox(e, [fornece_sal_mineral_sim, fornece_sal_mineral_nao])

    tipo_alimentacao_container = ft.Container(
        content=ft.Column([
            ft.Text("Tipo de Alimentação", **estilo_content),
            tipo_alimentacao_concentrado,
            tipo_alimentacao_volumoso,
            ft.Text("Fornece Sal Mineral?", **estilo_content),
            fornece_sal_mineral_sim,
            fornece_sal_mineral_nao,
        ]),        
        **estilo_container
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
                qtde_total_animais,
                raca_predominante,
                sistema_criacao_container,
                usa_racao_container,
                tipo_alimentacao_container,                  
                botao,
                t
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15            
        )
    )    
