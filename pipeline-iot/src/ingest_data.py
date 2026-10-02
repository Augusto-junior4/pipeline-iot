import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Configuração da conexão com o PostgreSQL (Docker)
# Formato: postgresql://usuario:senha@localhost:5432/nome_do_banco
DB_URL = "postgresql://postgres:minhasenha@localhost:5432/postgres"
engine = create_engine(DB_URL)

# 2. Caminho do arquivo CSV
CSV_PATH = os.path.join("data", "IoT-temp.csv")

def main():
    print("Iniciando a leitura do arquivo CSV...")
    
    # Lê o arquivo CSV usando pandas
    df = pd.read_csv(CSV_PATH)
    
    print(f"Total de registros encontrados: {len(df)}")
    
    # Ajuste e limpeza básica de colunas
    # Ajusta os nomes das colunas para minúsculas para facilitar no SQL
    df.columns = [col.strip().lower().replace(" ", "_") for col.colunas if hasattr(df, 'colunas') else df.columns]
    
    # Trata a coluna de data/hora (se existir no dataset)
    if 'noted_date' in df.columns:
        df['timestamp'] = pd.to_datetime(df['noted_date'], errors='coerce')
    elif 'date' in df.columns:
        df['timestamp'] = pd.to_datetime(df['date'], errors='coerce')

    print("Inserindo dados no banco PostgreSQL...")
    
    # Envia os dados para a tabela 'temperature_readings' no PostgreSQL
    df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
    
    print("Dados inseridos com sucesso na tabela 'temperature_readings'!")

if __name__ == "__main__":
    main()