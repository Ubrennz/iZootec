import flet as ft
from components import base as tb
from components import cor_pagina as pagina
from database import conexao_db

def inventario(page: ft.Page, nome_propriedade: str):
    page.title = "Inventário"

    tb.topBar(page)
    pagina.corPagina(page)
    page.scroll = ft.ScrollMode.HIDDEN

    estilo_dados = {
        "size": 20,
        "weight": ft.FontWeight.BOLD,
        "color": ft.Colors.BLACK
    }
    
    conn = conexao_db.conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Propriedade WHERE nome_propriedade = ?", (nome_propriedade,))
    prop = cursor.fetchone()
    conn.close()

    if not prop:
        page.add(ft.Text(f"Propriedade '{nome_propriedade}' não encontrada.", color=ft.Colors.RED))
        return
    
    campos = [
        ("Nome da Propriedade", prop[3]),
        ("Proprietário", prop[4]),
        ("Endereço", prop[5]),
        ("Tamanho (ha)", prop[6]),
        ("Nº Piquetes", prop[7]),
        ("Nº Currais", prop[8]),
        ("Funcionários", prop[9]),
        ("Possui Máquinas", prop[10]),
        ("Quais Máquinas", prop[11]),
        ("Total Animais", prop[12]),
        ("Raça Predominante", prop[13]),
        ("Sistema Criação", prop[14]),
        ("Usa Ração", prop[15]),
        ("Tipo Alimentação", prop[16]),
        ("Fornece Sal Mineral", prop[17]),
        ("Controle Vacinas", prop[18]),
        ("Data Última Vacina", prop[19]),
        ("Vacas em Lactação", prop[20]),
        ("Vacas Secas", prop[21]),
        ("Total Vacas", prop[22]),
        ("Produção Diária Total (L)", prop[23]),
        ("Média Produção por Vaca (L)", prop[24]),
        ("Ordenhas por Dia", prop[25]),
        ("Tipo Ordenha", prop[26]),
        ("Pré/Pós-Dipping", prop[27]),
        ("Local Ordenha", prop[28]),
        ("Leite Descartado (L)", prop[29]),
        ("Suplementação Vacas Lactação", prop[30]),
        ("Pasto p/ Vacas Leiteiras", prop[31]),
        ("Tipo Confinamento", prop[32]),
    ]

    inventario_list = [
        ft.Row([
            ft.Text(label + ":", **estilo_dados, width=250),
            ft.Text(str(valor), **estilo_dados)
        ]) for label, valor in campos if valor is not None
    ]

    page.add(
        ft.Column(
            controls=[
                ft.Text(f"Inventário Zootécnico - {nome_propriedade}", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
                ft.Divider(),
                *inventario_list
            ],
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=8            
        )
    )