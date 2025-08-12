orders_query = """
            CREATE TABLE IF NOT EXISTS orders
            (
                id           SERIAL PRIMARY KEY,
                user_id      INT ,
                user_name      VARCHAR(128) NOT NULL,
                kitchen_name   VARCHAR(256)  NOT NULL,
                food_name     VARCHAR(256) NOT NULL,
                quantity      INT,
                status       VARCHAR(64) CHECK (status in ('pending', 'ready')),
                price        DECIMAL(8, 2),
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) \
            """

# ready_orders_query = """
#             CREATE TABLE IF NOT EXISTS ready_order
#             (
#                 id           SERIAL PRIMARY KEY,
#                 user_id      INT 
#                 user_name         VARCHAR(128) NOT NULL,
#                 kitchen_name   VARCHAR(256)  NOT NULL,
#                 food_name     VARCHAR(256) NOT NULL,
#                 quantity      INT,
#                 status       VARCHAR(64) CHECK (status in ('pending', 'ready')),
#                 price        FLOAT(8,2),
#                 created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             ) \
#             """