import flet as ft
from components import base as tb
from components import cor_pagina as pagina

def homepage(page: ft.Page):
    page.title = "Homepage Técnico" 

    tb.topBar(page)
    pagina.corPagina(page)

    def button_clicked(e):
        page.clean()
    

    botao = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text("Fazenda", color=ft.Colors.WHITE),
            alignment=ft.alignment.center_left,  # ⬅️ Aqui você muda o alinhamento
            expand=True,
        ),
        on_click=button_clicked,
        bgcolor=ft.Colors.GREEN,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8)
        ),
        height=50,
        width=500,
    )

    page.add(
        ft.Column(
            controls=[
                botao
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )