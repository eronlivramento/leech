import psycopg2


class PostgreSQL:
    def __init__(
        self, host: str, port: str, database: str, user: str, password: str
    ) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):

        try:
            return psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
            )
        except (Exception, psycopg2.DatabaseError) as error:
            raise error
