import flet as ft
from components import base as tb
from components import cor_pagina as pagina
from database import conexao_db

from pages import cadastro_propriedade as propriedade

def cadastroPessoa(page: ft.Page):
    page.title = "Casdastro" 

    tb.topBar(page)
    pagina.corPagina(page)   

    def button_clicked(e):
        try:
            conn = conexao_db.conexao()
            cursor = conn.cursor()

            if tipo_pessoa_produtor.value:
                cursor.execute('''
                    INSERT INTO Produtor (nome_produtor, cpf_produtor, telefone_produtor, email_produtor, senha_produtor)
                    VALUES (?, ?, ?, ?, ?)''', (nome.value, cpf.value, telefone.value, email.value, senha.value,))

                conn.commit()
                conn.close()

                page.clean()
                propriedade.cadastroPropriedade(page)
            elif tipo_pessoa_tecnico.value:
                cursor.execute('''
                    INSERT INTO Tecnico (nome_tecnico, cpf_tecnico, telefone_tecnico, email_tecnico, senha_tecnico)
                    VALUES (?, ?, ?, ?, ?)''', (nome.value, cpf.value, telefone.value, email.value, senha.value,))
                
                conn.commit()
                conn.close()

                page.clean()
        except Exception as e:
            print(f"erro: {e}")
        
    def checkbox(e, lista_checkbox):
        for checkbox in lista_checkbox:
            if checkbox != e.control:
                checkbox.value = False

        page.update()      

    t = ft.Text()

    estilo_sub_titulo = {
        "size": 40,
        "color": ft.Colors.BLACK
    }

    estilo_padrao = {
        "border_color": ft.Colors.GREY,
        "focused_border_color": ft.Colors.GREEN,
        "cursor_color": ft.Colors.GREEN,
        "border_radius": 8,        
        "bgcolor": ft.Colors.WHITE,
        "color": ft.Colors.BLACK,        
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

    cadastro_do_tecnico = ft.Text("Preencha Seus Dados", **estilo_sub_titulo)

    nome = ft.TextField(hint_text="Nome Completo", **estilo_padrao)
    cpf = ft.TextField(hint_text="CPF", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    telefone = ft.TextField(hint_text="Telefone", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    email = ft.TextField(hint_text="E-mail", **estilo_padrao)
    senha = ft.TextField(hint_text="Senha", **estilo_padrao, password=True, can_reveal_password=True)

    tipo_pessoa_produtor = ft.Checkbox(label="Produtor", **estilo_label)
    tipo_pessoa_tecnico = ft.Checkbox(label="Técnico", **estilo_label)
    tipo_pessoa_produtor.on_change = lambda e: checkbox(e, [tipo_pessoa_produtor, tipo_pessoa_tecnico])
    tipo_pessoa_tecnico.on_change = lambda e: checkbox(e, [tipo_pessoa_produtor, tipo_pessoa_tecnico])

    tipo_pessoa_container = ft.Container(
        content=ft.Column([
            ft.Text("Você é:", **estilo_content),
            tipo_pessoa_produtor,
            tipo_pessoa_tecnico,
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
                cadastro_do_tecnico,
                nome,
                cpf,
                telefone,
                email,
                senha,
                tipo_pessoa_container,
                botao,                
                t
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )
