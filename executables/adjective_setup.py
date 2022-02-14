

from models.adjectives import Adjectives
from temp.vars import *

db_adjective_engine = Adjectives.database_config(name='adjetivos.db')
db_adjective_cursor = Adjectives.database_cursor(engine_var=db_adjective_engine)
Adjectives.database_init(engine_var=db_adjective_engine)

if __name__ == '__main__':
    Adjectives.database_insert_many(exec_=db_adjective_cursor,
                                    length=len(adjectives),
                                    adjective_box=adjectives,
                                    adjective_tr_box=adjectives_pt_br)
    # pass
