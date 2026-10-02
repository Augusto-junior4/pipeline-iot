from sqlalchemy import create_engine, text

# Conexão com o PostgreSQL
DB_URL = "postgresql://postgres:minhasenha@localhost:5432/postgres"
engine = create_engine(DB_URL)

# Queries SQL para criação das 3 Views exigidas
views_sql = [
    """
    CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
    SELECT id AS device_id, AVG(temp) AS avg_temp
    FROM temperature_readings
    GROUP BY id;
    """,
    """
    CREATE OR REPLACE VIEW leituras_por_hora AS
    SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
    FROM temperature_readings
    WHERE timestamp IS NOT NULL
    GROUP BY hora
    ORDER BY hora;
    """,
    """
    CREATE OR REPLACE VIEW temp_max_min_por_dia AS
    SELECT DATE(timestamp) AS data, MAX(temp) AS temp_max, MIN(temp) AS temp_min
    FROM temperature_readings
    WHERE timestamp IS NOT NULL
    GROUP BY data
    ORDER BY data;
    """
]

def main():
    with engine.connect() as connection:
        for sql in views_sql:
            connection.execute(text(sql))
            connection.commit()
    print("Views SQL criadas com sucesso no PostgreSQL!")

if __name__ == "__main__":
    main()from sqlalchemy import create_engine, text

# Conexão com o PostgreSQL
DB_URL = "postgresql://postgres:minhasenha@localhost:5432/postgres"
engine = create_engine(DB_URL)

# Queries SQL para criação das 3 Views exigidas
views_sql = [
    """
    CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
    SELECT id AS device_id, AVG(temp) AS avg_temp
    FROM temperature_readings
    GROUP BY id;
    """,
    """
    CREATE OR REPLACE VIEW leituras_por_hora AS
    SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
    FROM temperature_readings
    WHERE timestamp IS NOT NULL
    GROUP BY hora
    ORDER BY hora;
    """,
    """
    CREATE OR REPLACE VIEW temp_max_min_por_dia AS
    SELECT DATE(timestamp) AS data, MAX(temp) AS temp_max, MIN(temp) AS temp_min
    FROM temperature_readings
    WHERE timestamp IS NOT NULL
    GROUP BY data
    ORDER BY data;
    """
]

def main():
    with engine.connect() as connection:
        for sql in views_sql:
            connection.execute(text(sql))
            connection.commit()
    print("Views SQL criadas com sucesso no PostgreSQL!")

if __name__ == "__main__":
    main()