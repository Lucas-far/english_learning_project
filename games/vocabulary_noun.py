

from models.nouns import Nouns
from executables.noun_setup import noun_db_cursor

noun_db = []

question_which_noun = """
======= QUAL O SIGNIFICADO DO SUBSTANTIVO "{}" =======
a) {}
b) {}
c) {}
d) {}
e) {}
"""


class Game:

    def __init__(self):
        self.__score_plus = 0
        self.__score_minus = 0


print(Nouns.database_as_var(noun_db_cursor))
