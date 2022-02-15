

from models.nouns import Nouns
from executables.noun_setup import noun_db_cursor
from functions.database import ink
# from games.vocabulary_noun import noun_db

noun_database = Nouns.database_as_var(noun_db_cursor)


if __name__ == '__main__':
    if len(noun_database) == 0:
        print('Banco de dados de substantivo vazio.')
    else:
        for data in noun_database:
            print(ink(data))
