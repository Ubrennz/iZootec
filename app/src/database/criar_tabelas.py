from database import conexao_db

def criar_tabela():
    conn = conexao_db.conexao()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tecnico (
            id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_tecnico TEXT NOT NULL,
            cpf_tecnico VACHAR(14) NOT NULL UNIQUE,
            telefone_tecnico INTEGER,
            email_tecnico TEXT NOT NULL,
            senha_tecnico TEXT NOT NULL                   
        )    
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produtor (
            id_produtor INTEGER PRIMARY KEY AUTOINCREMENT,
            id_tecnico INTEGER,
            nome_produtor TEXT NOT NULL,
            cpf_produtor VACHAR(14) NOT NULL UNIQUE,
            telefone_produtor INTEGERs,
            email_produtor TEXT NOT NULL,
            senha_produtor TEXT NOT NULL,            
            FOREIGN KEY(id_tecnico) REFERENCES Tecnico(id_tecnico)              
        )    
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Propriedade (
            id_propriedade INTEGER PRIMARY KEY AUTOINCREMENT,
            id_produtor INTEGER,
            id_tecnico INTEGER,
            nome_propriedade TEXT,
            nome_propriedario TEXT,
            endereco_propriedade TEXT,
            tamanho_propriedade_em_hectares FLOAT,
            numero_piquetes INTEGER,
            numero_curais INTEGER,
            qtde_funcionarios INTEGER,
            possui_maquinas TEXT, -- BOOLEAN
            quais_maquinas TEXT,
            numero_total_animais INTEGER,
            raca_predominante TEXT,
            sistema_criacao TEXT, -- ENUM 
            usa_racao TEXT, -- BOOLEAN
            tipo_alimentacao TEXT,
            fornece_sal TEXT, -- BOOLEAN
            faz_controle_vacinas TEXT, -- BOOLEAN
            data_ultima_vacina_rebanho DATE,
            qtde_total_vacas_em_lactacao INTEGER,
            numero_vacas_secas INTEGER,
            numero_total_vacas INTEGER,
            producao_diario_total_litros FLOAT,
            media_producao_por_vaca FLOAT,
            qtde_ordenhas_por_dia INTEGER,
            tipo_ordenha TEXT,
            uso_pre_e_pos_dipping TEXT, -- BOOLEAN
            local_ordenha TEXT, -- ENUM
            leite_descartado_por_contaminacao_litros FLOAT,
            suplementacao_vacas_em_lactacao TEXT,
            pasto_disponivel_para_vacas_leiteiras TEXT, -- BOOLEAN
            tipo_confinamento TEXT,
            FOREIGN KEY(id_produtor) REFERENCES Produtor(id_produtor),
            FOREIGN KEY(id_tecnico) REFERENCES Tecnico(id_tecnico)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabela()
