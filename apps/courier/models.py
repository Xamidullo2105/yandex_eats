courier_query = """
            CREATE TABLE IF NOT EXISTS couriers
            (
                id           SERIAL PRIMARY KEY,
                name         VARCHAR(128) NOT NULL,
                email        VARCHAR(256)  NOT NULL,
                password     VARCHAR(256) NOT NULL,
                is_login     BOOLEAN   DEFAULT FALSE,
                role       VARCHAR(64) CHECK (role IN ('user', 'kitchen', 'courier')),  
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) \
            """