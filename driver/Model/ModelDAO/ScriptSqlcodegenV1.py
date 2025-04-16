from sqlalchemy import create_engine, inspect
import os

# Configurações
DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5433/nw"
SCHEMA = "northwind"
ARQUIVO_DESTINO = "C:/Users/kendi/Desktop/BD2 - ATIVIDADE 1/Driver/Models/SqlcodegenTables.py"

# Conecta ao banco
engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

# Recupera as tabelas do schema
tabelas = inspector.get_table_names(schema=SCHEMA)

# Início do conteúdo do arquivo
linhas = ['# Modelagem das Tables do Schema em classes\n\n']

# Para cada tabela, gera uma classe com os campos no __init__
for tabela in tabelas:
    colunas = inspector.get_columns(tabela, schema=SCHEMA)
    nome_classe = tabela.capitalize()

    atributos = [col['name'] for col in colunas]
    argumentos = ", ".join(atributos)

    linhas.append(f'class {nome_classe}:\n')
    linhas.append(f'    def __init__(self, {argumentos}):\n')

    for atributo in atributos:
        linhas.append(f'        self.{atributo} = {atributo}\n')
    linhas.append('\n')

# Cria o diretório se não existir
os.makedirs(os.path.dirname(ARQUIVO_DESTINO), exist_ok=True)

# Escreve o conteúdo no arquivo
with open(ARQUIVO_DESTINO, 'w', encoding='utf-8') as f:
    f.writelines(linhas)

print(f"Arquivo gerado com sucesso: {ARQUIVO_DESTINO}")
