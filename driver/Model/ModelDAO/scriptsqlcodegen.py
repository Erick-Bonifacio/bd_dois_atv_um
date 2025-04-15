from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER, NUMERIC, SMALLINT, TIMESTAMP
import re

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5433/nw"
SCHEMA = "northwind"
ARQUIVO_DESTINO = "C:/Users/kendi/Desktop/BD2 - ATIVIDADE 1/Driver/Models/sqlcodegen_tables.py"

engine = create_engine(DATABASE_URL)
metadata = MetaData(schema=SCHEMA)
metadata.reflect(bind=engine)

Base = declarative_base()

linhas = []
linhas.append("from sqlalchemy import Column, Integer, String, Numeric, DateTime, SmallInteger")
linhas.append("from sqlalchemy.ext.declarative import declarative_base\n")
linhas.append("Base = declarative_base()\n")

def to_pascal_case(nome_tabela):
    partes = re.split(r'[_\s]', nome_tabela)
    return ''.join(p.capitalize() for p in partes if p)

for nome_tabela, tabela in metadata.tables.items():
    nome_classe = to_pascal_case(tabela.name)

    linhas.append(f"class {nome_classe}(Base):")
    linhas.append(f"    __tablename__ = '{tabela.name}'")
    linhas.append(f"    __table_args__ = {{'schema': '{SCHEMA}'}}\n")

    for coluna in tabela.columns:
        col_type = coluna.type
        if isinstance(col_type, VARCHAR):
            tipo_final = f"String({col_type.length})"
        elif isinstance(col_type, NUMERIC):
            tipo_final = f"Numeric({col_type.precision}, {col_type.scale})"
        elif isinstance(col_type, INTEGER):
            tipo_final = "Integer"
        elif isinstance(col_type, SMALLINT):
            tipo_final = "SmallInteger"
        elif isinstance(col_type, TIMESTAMP):
            tipo_final = "DateTime"
        else:
            tipo_final = "String"  

        linha_coluna = f"    {coluna.name} = Column({tipo_final}"
        if coluna.primary_key:
            linha_coluna += ", primary_key=True"
        linha_coluna += ")"
        linhas.append(linha_coluna)

    linhas.append("")  
with open(ARQUIVO_DESTINO, "w", encoding="utf-8") as f:
    f.write('\n'.join(linhas))

print(f"✔️ Arquivo gerado com sucesso em: {ARQUIVO_DESTINO}")
