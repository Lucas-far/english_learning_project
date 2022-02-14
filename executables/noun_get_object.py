

"""
Pesquisar substantivo
"""

from executables.noun_setup import noun_db_cursor
from functions.database import *
from strings.database import *
from models.nouns import Nouns


class FindNoun:

    # Informar estado atual do banco
    def algorithm_init(self):
        noun_database = len(Nouns.database_as_var(noun_db_cursor))
        if noun_database == 0:
            print('Banco de dados vazio. Insira um objeto.')
        else:
            FindNoun.query_noun(self)

    def query_noun(self):
        code_block_init(object_search_label.format('SUBSTANTIVO'),
                        session_end,
                        session_start.format('Pesquisar substantivo'))
        self.__input_launcher = input(input_text_operation)  # Escolher ação

        if self.__input_launcher == '0':  # Encerramento
            code_block_init(terminal, closure)
            exit(0)
        if self.__input_launcher == '1':  # Continuação
            FindNoun.get_noun(self)
        else:
            code_block_init(error, warn.format(0, 1))  # Instrução em caso de valor errado
            input(roll)
            FindNoun.query_noun(self)  # Repetir esta função

    def get_noun(self):
        self.__input_noun = input(input_text_noun)  # Prover o nome do substantivo
        noun_exists = Nouns.database_query_by_noun(exec_=noun_db_cursor, noun=self.__input_noun)  # Input procurado no banco

        if noun_exists:  # Substantivo existe
            self.__number_attempts = 0
            code_block_init(label_find_success.format('SUBSTANTIVO'), noun_exists)  # Exibir objeto
            input(roll)
            FindNoun.query_noun(self)  # Voltar ao início

        if self.__number_attempts >= 3:  # Tentativas excedentes
            code_block_init(error, attempts_exceeded.format(self.__number_attempts), search_in_the_database)
            self.__number_attempts = 0
            exit(0)  # Sair

        else:
            self.__number_attempts += 1  # Forma de dizer ao usuário que ele deve procurar o objeto no banco
            code_block_init(error,
                            not_found.format('substantivo', self.__input_noun),
                            attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
            FindNoun.get_noun(self)  # Repetir esta função

    def __init__(self):
        self.__input_launcher = None
        self.__input_noun = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    hotel_object_search = FindNoun()
    hotel_object_search.algorithm_init()
