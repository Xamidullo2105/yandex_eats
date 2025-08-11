users_query = """
            CREATE TABLE IF NOT EXISTS users
            (
                id           SERIAL PRIMARY KEY,
                name         VARCHAR(128) NOT NULL,
                email        VARCHAR(256)  NOT NULL,
                password     VARCHAR(256) NOT NULL,
                is_active    BOOLEAN   DEFAULT FALSE,
                is_login     BOOLEAN   DEFAULT FALSE,
                role       VARCHAR(64) CHECK (role IN ('user', 'kitchen', 'courier')),
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) \
            """

verification_codes_query = """
                        CREATE TABLE IF NOT EXISTS codes
                        (
                            id           SERIAL PRIMARY KEY,
                            code         CHAR(4)     NOT NULL,
                            email        VARCHAR(256) NOT NULL,
                            created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        ) \
                        """
