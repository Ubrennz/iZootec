import flet as ft
# from pages import cadastro_produtor as produtor
from pages import cadastro_tecnico as tecnico
from pages import cadastro_propriedade as propriedade

def main(page: ft.Page):
    propriedade.cadastroPropriedade(page)

ft.app(target=main, port=8551, host="0.0.0.0" )
