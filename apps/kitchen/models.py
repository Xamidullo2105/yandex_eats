kitchen_query = """
            CREATE TABLE IF NOT EXISTS kitchens
            (
                id           SERIAL PRIMARY KEY,
                name         VARCHAR(128) NOT NULL,
                email        VARCHAR(256)  NOT NULL,
                password     VARCHAR(256) NOT NULL,
                phone_number CHAR(13),
                is_login     BOOLEAN   DEFAULT FALSE,
                role       VARCHAR(64) CHECK (role IN ('user', 'kitchen', 'courier')), 
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) \
            """

foods_query = """
            CREATE TABLE IF NOT EXISTS foods
            (
                id           SERIAL PRIMARY KEY,
                name         VARCHAR(128) NOT NULL,
                kitchen_name   VARCHAR(256)  NOT NULL,
                food_name     VARCHAR(256) NOT NULL,
                quantity      INT,
                status       VARCHAR(64) CHECK (status in ('Optepa', 'Blissimo', 'Evos')),
                price        FLOAT(8,2),
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) \
            """