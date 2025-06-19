import flet as ft
from components import base as tb

def cadastroTecnico(page: ft.Page):
    page.title = "Casdastro do Técnico" 

    tb.topBar(page)

    page.add(
        ft.Text(
            "Cadastro do Técnico",
            size=40,
            color=ft.Colors.BLACK,            
        ),
        ft.Container(height=3),     
    )

    def button_clicked(e):
        t.value = f"Textboxes values are: '{nome.value}', '{cpf.value}', '{telefone.value}', '{email.value}', '{senha.value}'."
        page.update()

    t = ft.Text()

    estilo_padrao = {
        "border_color": ft.Colors.GREY,
        "focused_border_color": ft.Colors.GREEN,
        "cursor_color": ft.Colors.GREEN,
        "border_radius": 8,        
        "bgcolor": ft.Colors.WHITE,
        "color": ft.Colors.BLACK,        
    }

    nome = ft.TextField(hint_text="Nome Completo", **estilo_padrao)
    cpf = ft.TextField(hint_text="CPF", **estilo_padrao)
    telefone = ft.TextField(hint_text="Telefone", **estilo_padrao)
    email = ft.TextField(hint_text="E-mail", **estilo_padrao)
    senha = ft.TextField(hint_text="Senha", **estilo_padrao, password=True, can_reveal_password=True)

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
                nome,
                cpf,
                telefone,
                email,
                senha,
                botao,
                t
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )
