

from models.nouns import Nouns
from executables.noun_get_db import noun_db_cursor
from functions.database import code_block_init
from strings.database import *
from tools.database import *


class Noun:

    def launch_algorithm(self):
        # Instruções.
        code_block_init(object_add_label.format('SUBSTANTIVO'),
                        session_end,
                        session_start.format('Adicionar substantivo'))
        self.__launcher = input(input_text_operation)  # Informar a instrução

        if self.__launcher == '0':  # Encerrar algoritmo
            code_block_init(terminal, closure)
            exit(0)
        # Continuar.
        elif self.__launcher == '1':
            Noun.get_noun(self)
        # Instrução de opções de input corretas e reiniciação do algoritmo.
        else:
            code_block_init(error, warn.format(0, 1))
            Noun.launch_algorithm(self)

    def get_noun(self):
        # Informa o substantivo.
        self.__noun = input(input_text_noun)
        # Verificar se input existe como valor de alguma chave no banco
        self.__noun_exists = Nouns.database_query_by_noun(exec_=noun_db_cursor, noun=self.__noun)
        # Se o substantivo já existir, reiniciar esta função e fornecer um que não exista
        if self.__noun_exists:
            code_block_init(error, noun_object_repeated.format(self.__noun))
            Noun.get_noun(self)
        else:
            # Substantivo impróprio, retornar erro e instrução, reiniciar esta função.
            if self.__noun in not_allowed_inputs:
                code_block_init(error, invalid_data.format('Substantivo'))
                Noun.get_noun(self)
            else:
                # Substantivo apropriado, continuar.
                Noun.get_noun_tr(self)

    def get_noun_tr(self):
        # Informar a tradução do substantivo.
        self.__noun_tr = input(input_text_noun_tr)
        # Substantivo impróprio, retornar erro e instrução, reiniciar esta função.
        if self.__noun_tr in not_allowed_inputs:
            code_block_init(error, invalid_data.format('Tradução do substantivo'))
            Noun.get_noun_tr(self)
        # Substantivo e tradução apropriados, criar objeto passando os inputs como parâmetro, adicionar ao banco.
        else:
            new_noun = Nouns(noun=self.__noun, noun_tr=self.__noun_tr)
            Nouns.database_insert(exec_=noun_db_cursor, noun_object=new_noun)
            # Achando o objeto no banco e exibindo abaixo
            noun_json = Nouns.database_query_by_noun(exec_=noun_db_cursor, noun=self.__noun)
            code_block_init(terminal, noun_object_added.format(noun_json))
            Noun.launch_algorithm(self)

    def __init__(self):
        self.__launcher = None
        self.__noun = None
        self.__noun_tr = None
        self.__noun_exists = None


if __name__ == '__main__':
    object_add = Noun()
    object_add.launch_algorithm()
