
import psycopg2
from psycopg2 import Error
from psycopg2 import extras


class Db_connection_manager:

    host = "localhost"
    database = "prueba"
    user = "postgres"
    password = "1234"
    port = "5432"
    connection = None
    cursor = None

    def open(self):
        try:
            # Connect to an existing database
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port)
            print('connection successful')
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def close(self):
        if self.connection is not None:
            self.connection.close()
        if self.cursor is not None:
            self.cursor.close()

    def execute_query(self, query: str):
        try:
            self.cursor = self.connection.cursor(
                cursor_factory=extras.RealDictCursor)
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except (Exception, Error) as error:
            print("Error while executing query to PostgreSQL", error)
