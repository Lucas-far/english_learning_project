

from models.adjectives import Adjectives
from executables.adjective_setup import db_adjective_cursor
from functions.database import ink

if __name__ == '__main__':
    adjective_database = Adjectives.database_as_var(db_adjective_cursor)

    if len(adjective_database) == 0:
        print('Banco de dados de adjetivo vazio.')
    else:
        for data in adjective_database:
            print(ink(data))
