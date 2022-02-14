

from models.nouns import Nouns
from temp.vars import *

noun_db_engine = Nouns.database_config(name='substantivos.db')
noun_db_cursor = Nouns.database_cursor(engine_var=noun_db_engine)
Nouns.database_init(engine_var=noun_db_engine)


if __name__ == '__main__':
    Nouns.database_insert_many(exec_=noun_db_cursor,
                               length=len(nouns),
                               noun_box=nouns,
                               noun_tr_box=nouns_pt_br)
    # pass
