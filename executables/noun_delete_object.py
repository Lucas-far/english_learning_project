

"""
Deletar substantivo
"""

from models.nouns import Nouns
from executables.noun_setup import noun_db_cursor
from functions.database import *
from strings.database import *
from tools.database import *


class Noun:

    def is_database_empty(self):
        database_size = len(Nouns.database_as_var(exec_=noun_db_cursor))

        if database_size == 0:
            code_block_init(terminal, empty_database)
            exit(0)
        else:
            Noun.launch_algorithm(self)

    def launch_algorithm(self):
        code_block_init(object_edit_label.format('SUBSTANTIVO'),
                        session_end,
                        session_start.format('Deletar substantivo'))  # Instruções
        self.__input_launcher = input(input_text_operation)  # Escolher procedimento baseado nas instruções

        if self.__input_launcher == '0':
            code_block_init(terminal, closure)  # Encerrar algoritmo
            exit(0)
        if self.__input_launcher == '1':  # Continuar
            Noun.get_noun(self)
        else:  # Lançar erro e reinicar, até digitar a opção certa
            code_block_init(error, warn.format(0, 1))
            Noun.launch_algorithm(self)

    def get_noun(self):
        self.__noun = input(noun_to_be_deleted)  # Coletar o nome do substantivo

        # Cursor busco no banco se há objeto com chave de valor == input.
        # Se achar, retorna o objeto já em formato json, senão, retorna None
        self.__noun_data = Nouns.database_query_by_noun(exec_=noun_db_cursor, noun=self.__noun)

        if self.__noun_data:
            self.__number_attempts = 0
            Noun.delete_session(self)  # Continuar

        # Lançar erro e parar o algoritmo (deve vir antes da condição que incrementa seu valor, para evitar problemas)
        if self.__number_attempts >= 3:
            code_block_init(error, attempts_exceeded.format(self.__number_attempts), search_in_the_database)
            self.__number_attempts = 0
            exit(0)

        if not self.__noun_data:  # Abrir uma contagem, se errar 3 vezes, o algoritmo encerra
            self.__number_attempts += 1
            code_block_init(error,
                            not_found.format('SUBSTANTIVO', self.__noun),
                            attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
            Noun.get_noun(self)   # Repetir até o substantivo de nome correto for informado

    def delete_session(self):
        code_block_init(label_find_success.format('SUBSTANTIVO'), self.__noun_data)  # Exibir o substantivo
        self.__decision = input(ask_if_remove)                  # Decidir entre 0 ou 1

        if self.__decision == '0':
            code_block_init(terminal, object_removal_canceled)
            Noun.launch_algorithm(self)                                       # reiniciar algoritmo
        elif self.__decision == '1':
            Nouns.object_noun_delete(exec_=noun_db_cursor, noun=self.__noun)  # remoção do substantivo
            Noun.launch_algorithm(self)                                      # reiniciar algoritmo
        else:
            code_block_init(terminal, warn.format(0, 1))
            Noun.delete_session(self)   # repetir esta função até que um input correto seja fornecido

    def __init__(self):
        self.__input_launcher = None
        self.__noun = None
        self.__noun_data = None
        self.__decision = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    object_exclusion = Noun()
    object_exclusion.is_database_empty()
