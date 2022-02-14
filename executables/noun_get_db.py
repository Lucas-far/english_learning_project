

from models.nouns import Nouns
from executables.noun_setup import noun_db_cursor
from functions.database import ink

if __name__ == '__main__':
    noun_database = Nouns.database_as_var(noun_db_cursor)

    if len(noun_database) == 0:
        print('Banco de dados de substantivo vazio.')
    else:
        for data in noun_database:
            print(ink(data))
