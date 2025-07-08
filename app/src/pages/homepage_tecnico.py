import flet as ft
from pages import inventario_propriedade
from components import base as tb
from components import cor_pagina as pagina
from database import conexao_db

def homepage(page: ft.Page):
    page.title = "Homepage Técnico" 

    tb.topBar(page)
    pagina.corPagina(page)
   
    def button_clicked(e, nome_propriedade):
        page.clean()

        inventario_propriedade.inventario(page, nome_propriedade)
        
    conn = conexao_db.conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT nome_propriedade FROM Propriedade")
    propriedades = cursor.fetchall()
    conn.close()
    
    botoes = []
    for propriedade in propriedades:
        nome_propriedade = propriedade[0]
        botao = ft.ElevatedButton(
            content=ft.Container(
                content=ft.Text(nome_propriedade, color=ft.Colors.WHITE),
                alignment=ft.alignment.center_left,
                expand=True,
            ),
            on_click=lambda e, nome=nome_propriedade: button_clicked(e, nome),
            bgcolor=ft.Colors.GREEN,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8)
            ),
            height=50,
            width=500,
        )
        botoes.append(botao)

    page.add(
        ft.Column(
            controls=botoes,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )