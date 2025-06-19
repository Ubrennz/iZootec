import flet as ft

def topBar(page: ft.Page):
    page.appbar = ft.AppBar(        
        leading_width=40,
        title=ft.Text("iZootec", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor=ft.Colors.GREEN,                
    )

    page.bgcolor = ft.Colors.WHITE