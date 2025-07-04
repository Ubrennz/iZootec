import flet as ft
import re
from components import base as tb
from components import cor_pagina as pagina
from database import conexao_db

def cadastroPropriedade(page: ft.Page):
    page.title = "Casdastro da Propriedade"
    
    tb.topBar(page)
    pagina.corPagina(page)
    page.scroll = ft.ScrollMode.HIDDEN

    def button_clicked(e):
        try:
            sistema_criacao = (
                "Confinamento" if sistema_criacao_confinamento.value else
                "Semi-confinado" if sistema_criacao_semi_confinado.value else
                "Apasto" if sistema_criacao_apasto.value else
                "Não informado"
            )

            tipo_alimentacao = (
                "Concentrado" if tipo_alimentacao_concentrado.value else
                "Volumoso" if tipo_alimentacao_volumoso.value else
                "Não informado"
            )

            uso_pre_pos_dipping = (
                "Sim" if uso_pre_e_pos_dipping_sim.value else
                "Não" if uso_pre_e_pos_dipping_nao.value else
                "Não informado"
            )

            local_ordenha = (
                "Curral" if local_ordenha_sim.value else
                "Sala de Ordenha" if local_ordenha_nao.value else
                "Não informado"
            )

            possui_maquinas = (
                "Sim" if possui_maquinas_sim.value else
                "Não" if possui_maquinas_nao.value else
                "Não informado"
            )

            usa_racao = (
                "Sim" if usa_racao_sim.value else
                "Não" if usa_racao_nao.value else
                "Não informado"
            )

            fornece_sal = (
                "Sim" if fornece_sal_mineral_sim.value else
                "Não" if fornece_sal_mineral_nao.value else
                "Não informado"
            )

            faz_controle_vacinas = (
                "Sim" if faz_controle_vacina_sim.value else
                "Não" if faz_controle_vacina_nao.value else
                "Não informado"
            )

            pasto_disponivel = (
                "Sim" if pasto_disponivel_para_vacas_leiteiras_sim.value else
                "Não" if pasto_disponivel_para_vacas_leiteiras_nao.value else
                "Não informado"
            )

            conn = conexao_db.conexao()
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO Propriedade (
                    id_produtor,
                    id_tecnico,
                    nome_propriedade,
                    nome_propriedario,
                    endereco_propriedade,
                    tamanho_propriedade_em_hectares,
                    numero_piquetes,
                    numero_curais,
                    qtde_funcionarios,
                    possui_maquinas,
                    quais_maquinas,
                    numero_total_animais,
                    raca_predominante,
                    sistema_criacao,
                    usa_racao,
                    tipo_alimentacao,
                    fornece_sal,
                    faz_controle_vacinas,
                    data_ultima_vacina_rebanho,
                    qtde_total_vacas_em_lactacao,
                    numero_vacas_secas,
                    numero_total_vacas,
                    producao_diario_total_litros,
                    media_producao_por_vaca,
                    qtde_ordenhas_por_dia,
                    tipo_ordenha,
                    uso_pre_e_pos_dipping,
                    local_ordenha,
                    leite_descartado_por_contaminacao_litros,
                    suplementacao_vacas_em_lactacao,
                    pasto_disponivel_para_vacas_leiteiras,
                    tipo_confinamento
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                1,
                1,
                nome_propriedade.value,
                nome_proprietario.value,
                endereco_propriedade.value,
                float(tamanho_propriedade_em_hectares.value),
                int(numero_piquetes.value),
                int(numero_curais.value),
                int(qtde_funcionarios.value),
                possui_maquinas,
                quais_maquinas.value,
                int(numero_total_animais.value),
                raca_predominante.value,
                sistema_criacao,
                usa_racao,
                tipo_alimentacao,
                fornece_sal,
                faz_controle_vacinas,
                data_ultima_vacina_rebanho.value,
                int(numero_total_vacas_em_lactacao.value),
                int(numero_vacas_secas.value),
                int(numero_total_vacas.value),
                float(producao_diario_total_litros.value),
                float(media_producao_por_vaca.value),
                int(qtde_ordenhas_por_dia.value),
                tipo_ordenha.value,
                uso_pre_pos_dipping,
                local_ordenha,
                float(leite_descartado_por_contaminacao_litros.value),
                suplementacao_vacas_em_lactacao.value,
                pasto_disponivel,
                tipo_confinamento.value
            ))

            conn.commit()
            conn.close()

            t.value = "Propriedade cadastrada com sucesso!"

        except ValueError:
            t.value = "Erro: Verifique os campos numéricos obrigatórios."
        except Exception as ex:
            t.value = f"Erro: {ex}"

        page.update()


    def checkbox(e, lista_checkbox):
        for checkbox in lista_checkbox:
            if checkbox != e.control:
                checkbox.value = False

        page.update()

    def aplicar_mascara(e):
        texto = re.sub(r'\D', '', data_ultima_vacina_rebanho.value)
        novo_texto = ""

        if len(texto) >= 2:
            novo_texto += texto[:2] + "/"
        else:
            novo_texto += texto
        if len(texto) >= 4:
            novo_texto += texto[2:4] + "/"
        elif len(texto) > 2:
            novo_texto += texto[2:]
        if len(texto) >= 5:
            novo_texto += texto[4:8]
        
        data_ultima_vacina_rebanho.value = novo_texto
        data_ultima_vacina_rebanho.update()    

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
        "text_style": ft.TextStyle(weight=ft.FontWeight.BOLD)
    }

    estilo_checkbox = {
        "active_color": ft.Colors.GREEN_600,
        "check_color": ft.Colors.WHITE
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

    cadastro_da_propriedade = ft.Text("Cadastro da Propriedade", **estilo_sub_titulo)

    nome_propriedade = ft.TextField(hint_text="Nome da Propriedade", **estilo_padrao)
    nome_proprietario = ft.TextField(hint_text="Nome do Proprietario", **estilo_padrao)
    endereco_propriedade = ft.TextField(hint_text="Endereço da Propriedade", **estilo_padrao)
    tamanho_propriedade_em_hectares = ft.TextField(hint_text="Tamanho da Propriedade em Hectares", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_piquetes = ft.TextField(hint_text="Número de Piquetes", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_curais = ft.TextField(hint_text="Número de Curais", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    qtde_funcionarios = ft.TextField(hint_text="Quantidade de Funcionários", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
        
    possui_maquinas_sim = ft.Checkbox(label="Sim", **estilo_checkbox, **estilo_label)
    possui_maquinas_nao = ft.Checkbox(label="Não", **estilo_checkbox, **estilo_label)
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
    
    numero_total_animais = ft.TextField(hint_text="Número Total de Animais", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    raca_predominante = ft.TextField(hint_text="Raça Predominante", **estilo_padrao)

    sistema_criacao_confinamento = ft.Checkbox(label="Confinamento", **estilo_checkbox, **estilo_label)
    sistema_criacao_semi_confinado = ft.Checkbox(label="Semi-confinado", **estilo_checkbox, **estilo_label)
    sistema_criacao_apasto = ft.Checkbox(label="Apasto", **estilo_checkbox, **estilo_label)
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

    usa_racao_sim = ft.Checkbox(label="Sim", **estilo_checkbox, **estilo_label)
    usa_racao_nao = ft.Checkbox(label="Não", **estilo_checkbox, **estilo_label)
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

    tipo_alimentacao_concentrado = ft.Checkbox(label="Concentrado", **estilo_checkbox, **estilo_label)
    tipo_alimentacao_volumoso = ft.Checkbox(label="Volumoso", **estilo_checkbox, **estilo_label)
    tipo_alimentacao_concentrado.on_change = lambda e: checkbox(e, [tipo_alimentacao_concentrado, tipo_alimentacao_volumoso])
    tipo_alimentacao_volumoso.on_change = lambda e: checkbox(e, [tipo_alimentacao_concentrado, tipo_alimentacao_volumoso])

    fornece_sal_mineral_sim = ft.Checkbox(label="Sim", **estilo_checkbox, **estilo_label)
    fornece_sal_mineral_nao = ft.Checkbox(label="Não", **estilo_checkbox, **estilo_label)
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

    faz_controle_vacina_sim = ft.Checkbox(label="Sim", **estilo_checkbox, **estilo_label)
    faz_controle_vacina_nao = ft.Checkbox(label="Não", **estilo_checkbox, **estilo_label)
    faz_controle_vacina_sim.on_change = lambda e: checkbox(e, [faz_controle_vacina_sim, faz_controle_vacina_nao])
    faz_controle_vacina_nao.on_change = lambda e: checkbox(e, [faz_controle_vacina_sim, faz_controle_vacina_nao])

    faz_controle_vacina_container = ft.Container(
        content=ft.Column([
            ft.Text("Faz Controle de Vacinas?", **estilo_content),
            faz_controle_vacina_sim,
            faz_controle_vacina_nao,            
        ]),        
        **estilo_container       
    )

    data_ultima_vacina_rebanho = ft.TextField(hint_text="Data da Última Vacina do Rebanho", **estilo_padrao, height=80, keyboard_type=ft.KeyboardType.NUMBER, on_change=aplicar_mascara)
    
    estrutura_do_rebanho_leiteiro = ft.Text("Estrutura do Rebanho Leiteiro", **estilo_sub_titulo)

    numero_total_vacas_em_lactacao = ft.TextField(hint_text="Número Total das Vacas em Lactação", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_vacas_secas = ft.TextField(hint_text="Número Total de Vacas Secas", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    numero_total_vacas = ft.TextField(hint_text="Número Total de Vacas", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    producao_diario_total_litros = ft.TextField(hint_text="Produção Diária Total (Média)", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    media_producao_por_vaca = ft.TextField(hint_text="Média de Produçao por Vaca", **estilo_padrao, keyboard_type=ft.KeyboardType.NUMBER)
    qtde_ordenhas_por_dia = ft.TextField(hint_text="Quantidade de Ordenha por Dia", **estilo_padrao,keyboard_type=ft.KeyboardType.NUMBER)
    tipo_ordenha = ft.TextField(hint_text="Tipo de Ordenha", **estilo_padrao, height=80)

    higiene_e_manejo = ft.Text("Higiene e Manejo", **estilo_sub_titulo)
    
    uso_pre_e_pos_dipping_sim = ft.Checkbox(label="Sim", **estilo_checkbox, **estilo_label)
    uso_pre_e_pos_dipping_nao = ft.Checkbox(label="Não", **estilo_checkbox, **estilo_label)
    uso_pre_e_pos_dipping_sim.on_change = lambda e: checkbox(e, [uso_pre_e_pos_dipping_sim, uso_pre_e_pos_dipping_nao])
    uso_pre_e_pos_dipping_nao.on_change = lambda e: checkbox(e, [uso_pre_e_pos_dipping_sim, uso_pre_e_pos_dipping_nao])

    uso_pre_e_pos_dipping_container = ft.Container(
        content=ft.Column([
            ft.Text("Uso de Pré e Pós-Dipping", **estilo_content),
            uso_pre_e_pos_dipping_sim,
            uso_pre_e_pos_dipping_nao,
        ]),
        **estilo_container
    )

    local_ordenha_sim = ft.Checkbox(label="Curral", **estilo_checkbox, **estilo_label)
    local_ordenha_nao = ft.Checkbox(label="Sala de Ordenha", **estilo_checkbox, **estilo_label)
    local_ordenha_sim.on_change = lambda e: checkbox(e, [local_ordenha_sim, local_ordenha_nao])
    local_ordenha_nao.on_change = lambda e: checkbox(e, [local_ordenha_sim, local_ordenha_nao])

    local_ordenha_container = ft.Container(
        content=ft.Column([
            ft.Text("Local da Ordenha", **estilo_content),
            local_ordenha_sim,
            local_ordenha_nao,
        ]),
        **estilo_container
    )

    leite_descartado_por_contaminacao_litros = ft.TextField(hint_text="Leite Descardado por Contaminação (Litros)", **estilo_padrao, height=80, keyboard_type=ft.KeyboardType.NUMBER)

    nutricao_e_bem_estar = ft.Text("Nutrição e Bem-Estar", **estilo_sub_titulo)

    suplementacao_vacas_em_lactacao = ft.TextField(hint_text="Suplementão das Vacas em Lactação", **estilo_padrao)

    pasto_disponivel_para_vacas_leiteiras_sim = ft.Checkbox(label="Sim", **estilo_checkbox, **estilo_label)
    pasto_disponivel_para_vacas_leiteiras_nao = ft.Checkbox(label="Não", **estilo_checkbox, **estilo_label)
    pasto_disponivel_para_vacas_leiteiras_sim.on_change = lambda e: checkbox(e, [pasto_disponivel_para_vacas_leiteiras_sim, pasto_disponivel_para_vacas_leiteiras_nao])
    pasto_disponivel_para_vacas_leiteiras_nao.on_change = lambda e: checkbox(e, [pasto_disponivel_para_vacas_leiteiras_sim, pasto_disponivel_para_vacas_leiteiras_nao])

    pasto_disponivel_para_vacas_leiteiras_container = ft.Container(
        content=ft.Column([
            ft.Text("Pasto Disponível para Vacas Leiteiras", **estilo_content),
            pasto_disponivel_para_vacas_leiteiras_sim,
            pasto_disponivel_para_vacas_leiteiras_nao,
        ]),
        **estilo_container
    )

    tipo_confinamento = ft.TextField(hint_text="Tipo de Confinamento", **estilo_padrao)

    botao = ft.ElevatedButton(
        text="Salvar Dados",
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
                cadastro_da_propriedade,
                nome_propriedade,
                nome_proprietario,
                endereco_propriedade,
                tamanho_propriedade_em_hectares,
                numero_piquetes,
                numero_curais,
                qtde_funcionarios,
                possui_maquinas_container,                
                numero_total_animais,
                raca_predominante,
                sistema_criacao_container,
                usa_racao_container,
                tipo_alimentacao_container,
                faz_controle_vacina_container,
                data_ultima_vacina_rebanho,
                estrutura_do_rebanho_leiteiro,
                numero_total_vacas_em_lactacao,
                numero_vacas_secas,
                numero_total_vacas,
                producao_diario_total_litros,
                media_producao_por_vaca,
                qtde_ordenhas_por_dia,
                tipo_ordenha,
                higiene_e_manejo,
                uso_pre_e_pos_dipping_container,
                local_ordenha_container,
                leite_descartado_por_contaminacao_litros,
                nutricao_e_bem_estar,
                suplementacao_vacas_em_lactacao,
                pasto_disponivel_para_vacas_leiteiras_container,
                tipo_confinamento,
                botao,
                t            
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )    
