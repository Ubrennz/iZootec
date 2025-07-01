import flet as ft
from components import cor_pagina as pagina
from pages import cadastro_produtor as produtor

def primeiraTela(page: ft.Page):
    page.title = "Primeira Tela"

    pagina.corPagina(page)
    
    def button_clicked(e):
        page.clean()

        produtor.cadastroProdutor(page)

    def botao(texto):
        return ft.ElevatedButton(
            text=texto,
            on_click=button_clicked,        
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.GREEN,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=40),
                text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)                
            ),
            height=60,
            width=180
        )    

    estilo_font_izootec = {
        "size": 90,
        "color": ft.Colors.GREEN,
        "weight": ft.FontWeight.BOLD
    }

    estilo_descricao = {
        "size": 20,
        "color": ft.Colors.BLACK,
        "weight": ft.FontWeight.BOLD
    }

    t = ft.Text()

    imagem = ft.Container(
        content=ft.Image(
            src="https://i.imgur.com/xTjzx7z.png",
            width=400,
            height=300
        ),
        padding=ft.padding.only(top=100, bottom=60)
    )

    font_izootec = ft.Text("iZootec", **estilo_font_izootec)

    descricao_linha1 = ft.Text("Facilitando a gestão da sua propriedade", **estilo_descricao)
    descricao_linha2 = ft.Text("com zootecnia aplicada", **estilo_descricao, height=250)

    botao_cadastra_se = botao("Cadastra-se")
    botao_entrar = botao("Entrar")

    page.add(        
        ft.Container(
            content=ft.Column(
                controls=[
                    imagem,
                    font_izootec,
                    descricao_linha1,
                    descricao_linha2,                
                    botao_cadastra_se,
                    botao_entrar,
                    t
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,                
            ),
            alignment=ft.alignment.center            
        )        
    )
