from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = '{}://{}:{}@{}:{}/{}'.format(
            'postgresql+psycopg2',
            'postgres',
            'postgres',
            '0.0.0.0',
            '2345',
            'clean_db'
        )

        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
    