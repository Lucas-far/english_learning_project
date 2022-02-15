

from models.nouns import Nouns
from temp.vars import *

noun_db_engine = Nouns.database_config(name='substantivos.db')
noun_db_cursor = Nouns.database_cursor(engine_var=noun_db_engine)
Nouns.database_init(engine_var=noun_db_engine)


if __name__ == '__main__':
    # print(len(nouns_singular), len(nouns_singular_translation), len(nouns_plural), len(nouns_plural_translation))
    # print(nouns_singular[27], nouns_singular_translation[27], nouns_plural[27], nouns_plural_translation[27])
    Nouns.database_insert_many(exec_=noun_db_cursor,
                               length=len(nouns_singular),
                               box_noun=nouns_singular,
                               box_noun_translation=nouns_singular_translation,
                               box_noun_plural=nouns_plural,
                               box_noun_plural_translation=nouns_plural_translation)
    # pass
