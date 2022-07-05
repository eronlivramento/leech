import psycopg2

from src.model.cep_range import CepRangeModel


class Repository:
    def __init__(self, conn, db_schema, input_table, input_fields) -> any:
        self.conn = conn
        self.db_schema = db_schema
        self.input_table = input_table
        self.input_fields = input_fields

    def insert(self, model: CepRangeModel):
        try:
            cursor = self.conn.cursor()
            query = self.get_query_insert()

            records = (
                model.state,
                model.location,
                model.range,
                model.state,
                model.location,
            )
            cursor.execute(query, records)

            self.conn.commit()

            return cursor.rowcount

        except (Exception, psycopg2.Error):
            cursor.execute("rollback")

        finally:
            if self.conn:
                cursor.close()

    def get_query_insert(self):
        query = f"INSERT INTO {self.db_schema}.{self.input_table} "
        query += f"({self.input_fields}) "
        query += "SELECT %s, %s,%s WHERE NOT EXISTS ( SELECT id "
        query += f"FROM {self.db_schema}.{self.input_table} "
        query += "WHERE state = %s and location = %s);"
        return query

    def get_all(self) -> list:
        result = []
        try:
            cursor = self.conn.cursor()
            query = f"SELECT id, {self.input_fields} "
            query += f"FROM {self.db_schema}.{self.input_table}"
            cursor.execute(query)
            records = cursor.fetchall()

            for row in records:
                cep = CepRangeModel(row[1], row[2], row[3], row[0])
                result.append(cep)

            return result
        except (Exception, psycopg2.Error):
            pass

        finally:
            if self.conn:
                cursor.close()
