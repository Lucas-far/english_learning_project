

"""
Editar substantivo
"""

from models.nouns import Nouns
from executables.noun_setup import noun_db_cursor
from functions.database import *
from strings.database import *
from tools.database import *


class Noun:

    # Banco de dados precisa ter elementos, para prosseguir
    def is_database_empty(self):
        database_size = len(Nouns.database_as_var(exec_=noun_db_cursor))
        if database_size == 0:
            code_block_init(terminal, empty_database)
            exit(0)
        # Se não estiver vazio, o algritmo pode continuar
        else:
            Noun.launch_algorithm(self)

    # Decidir se o algoritmo
    def launch_algorithm(self):
        code_block_init(object_edit_label.format('SUBSTANTIVO'),
                        session_end,
                        session_start.format('Atualizar substantivo'))  # Instruções
        self.__input_launcher = input(input_text_operation)  # Escolher procedimento baseado nas instruções

        if self.__input_launcher == '0':  # Encerrar algoritmo
            code_block_init(terminal, closure)
            exit(0)
        if self.__input_launcher == '1':  # Continuar
            Noun.get_noun(self)
        else:  # Lançar erro e reinicar, até digitar a opção certa
            code_block_init(error, warn.format(0, 1))
            Noun.launch_algorithm(self)

    def get_noun(self):
        self.__noun = input(input_text_noun)  # Coletar o nome do substantivo

        # Cursor busco no banco se há objeto com chave de valor == input.
        # Se achar, retorna o objeto já em formato json, senão, retorna None
        self.__noun_data = Nouns.database_query_by_noun(exec_=noun_db_cursor, noun=self.__noun)

        if self.__noun_data:  # Se o objeto existe, manipular dados e exibí-los
            self.__number_attempts = 0
            self.__noun_data = list(self.__noun_data.items())
            self.__noun_data = [data for data in self.__noun_data]
            del self.__noun_data[0]

            # Obtenção da tradução do substantivo para uso na última parte da função (editar tradução)
            target_values = [self.__noun_data[index][1] for index in range(0, len(self.__noun_data))]
            self.__noun_tr_element = target_values[1]

            Noun.edit_choice(self)  # Continuar

        # Lançar erro e parar o algoritmo (deve vir antes da condição que incrementa seu valor, para evitar problemas)
        if self.__number_attempts >= 3:
            code_block_init(error, attempts_exceeded.format(self.__number_attempts), search_in_the_database)
            self.__number_attempts = 0
            exit(0)

        if not self.__noun_data:  # Abrir uma contagem, se errar 3 vezes, o algoritmo encerra
            self.__number_attempts += 1
            code_block_init(error,
                            not_found.format('substantivo', self.__noun),
                            attempts_remaining.format(self.__number_attempts_max - self.__number_attempts))
            Noun.get_noun(self)  # Repetir até o substantivo de nome correto for informado

    def edit_choice(self):
        # Não é preciso retornar a função anterior em caso de erro, pois o substantivo foi achado
        print('\n', label_find_success.format('SUBSTANTIVO'))  # Informar que o substantivo foi encontrado
        for each_attrib in self.__noun_data:  # Exibição dos dados na função anterior
            print(str(each_attrib))

        # Instruções (qual elemento deve ser editado)
        code_block_init('\n', options,
                        edit_element.format('substantivo'),
                        edit_element_tr.format('substantivo'),
                        edit_both)
        self.__which_to_edit = input(options_one_to_three)  # Informar o procedimento baseado na instrução

        if self.__which_to_edit in right_menu_numbers:  # Procedimento deve estar entre 1 a 3
            Noun.edit_session(self)  # Se estiver, continuar
        else:                        # Senão
            Noun.edit_choice(self)   # Repetir esta função

    def edit_session(self):
        # Editar somente o substantivo
        if self.__which_to_edit == '1':
            self.__new_noun = input(new_value.format('o substantivo', ink(hint)))
            # par2 (Nouns.noun == par2) / Par3 e par4 (Nouns.update(par3: par4))
            Nouns.object_noun_update(exec_=noun_db_cursor, noun=self.__noun, _key="noun", _value=self.__new_noun)
            input(roll)

        # Editar somente a tradução do substantivo
        elif self.__which_to_edit == '2':
            self.__new_noun_translation = input(new_value.format('o substantivo', ink(hint)))
            # par2 (Nouns.noun_tr == par2) / Par3 e par4 (Nouns.update(par3: par4))
            Nouns.object_noun_translation_update(exec_=noun_db_cursor,
                                        noun_tr=self.__noun_tr_element,
                                        _key="noun_tr",
                                        _value=self.__new_noun_translation)
            input(roll)

        # Editar ambos
        elif self.__which_to_edit == '3':
            # self.__noun_tr_element: adquirido em "get_noun()" pelo nome do substantivo (pego sem pedir input)
            self.__new_noun = input(new_value.format('substantivo', ink(hint)))
            self.__new_noun_translation = input(new_value.format('a tradução do substantivo', ink(hint)))
            Nouns.object_noun_update(
                exec_=noun_db_cursor,
                noun=self.__noun,
                _key="noun",
                _value=self.__new_noun
            )
            Nouns.object_noun_translation_update(
                exec_=noun_db_cursor,
                noun_tr=self.__noun_tr_element,
                _key="noun_tr",
                _value=self.__new_noun_translation
            )
            input(roll)

        # Uma das opções será escolhida, reiniciar algoritmo pode estar aqui, ao invés de dentro de cada condição
        Noun.launch_algorithm(self)

    def __init__(self):
        self.__input_launcher = None
        self.__noun = None
        self.__noun_tr_element = None
        self.__which_to_edit = None
        self.__new_noun = None
        self.__new_noun_translation = None
        self.__noun_data = None
        self.__number_attempts = 0
        self.__number_attempts_max = 3


if __name__ == '__main__':
    edit_noun = Noun()
    edit_noun.is_database_empty()
