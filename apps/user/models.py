unfinished_order_query = """
            CREATE TABLE IF NOT EXISTS unfinished_order
            (
                id           SERIAL PRIMARY KEY,
                user_id      INT 
                name         VARCHAR(128) NOT NULL,
                kitchen_name   VARCHAR(256)  NOT NULL,
                food_name     VARCHAR(256) NOT NULL,
                quantity      INT,
                status       VARCHAR(64) CHECK (status in ('pending', 'ready')),
                price        FLOAT(8,2),
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) \
            """

ready_orders_query = """
            CREATE TABLE IF NOT EXISTS unfinished_order
            (
                id           SERIAL PRIMARY KEY,
                user_id      INT 
                name         VARCHAR(128) NOT NULL,
                kitchen_name   VARCHAR(256)  NOT NULL,
                food_name     VARCHAR(256) NOT NULL,
                quantity      INT,
                status       VARCHAR(64) CHECK (status in ('pending', 'ready')),
                price        FLOAT(8,2),
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) \
            """