import flet as ft
from database.init_db import initDB
from pages import primeira_tela as primeira

def main(page: ft.Page):    
    primeira.primeiraTela(page)

if __name__ == "__main__":
    initDB()
    ft.app(target=main, view=ft.WEB_BROWSER)
