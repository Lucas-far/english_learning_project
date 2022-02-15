

from random import choice, shuffle
from models.nouns import Nouns
from executables.noun_get_db import noun_database
from executables.noun_setup import noun_db_cursor
from strings.database import (
    closure_hint, thank_you_for_playing, question_which_noun, hint, terminal, allowed_alternatives, success, failure,
    current_score
)
from functions.database import code_block_init, ink
from tools.database import *


class Game:

    # Inserir substantivos numa lista
    @staticmethod
    def get_nouns_from_source():
        box_with_nouns = []
        # É o mesmo que: for data in Nouns.database_as_var(exec_=noun_db_cursor)
        for data in noun_database:
            # O banco possui campos das versões singular e plural
            box_with_nouns.append(data['noun'])
            box_with_nouns.append(data['noun_plural'])
        return box_with_nouns

    # Inserir traduções dos substantivos numa lista
    @staticmethod
    def get_nouns_translation_from_source():
        box_with_nouns_translation = []
        for data in noun_database:
            box_with_nouns_translation.append(data['noun_translation'])
            box_with_nouns_translation.append(data['noun_plural_translation'])
        return box_with_nouns_translation

    # Pegar um substantivo para usar: como alternativa ou opção certa
    @staticmethod
    def get_random_noun():
        the_noun = choice(Game.get_nouns_from_source())

        # the_noun = Nouns.database_query_by_noun(exec_=noun_db_cursor, noun=the_noun)
        # the_noun = the_noun['noun']
        return the_noun

    # Coletar dados para adquirir 5 opções para construir a alternativa
    def init_config(self):
        nouns_translations = []
        nouns_set = set({})

        # Vars necessárias para achar as traduções na ordem correta
        all_nouns = Game.get_nouns_from_source()
        all_nouns_translations = Game.get_nouns_translation_from_source()

        # Obtenção dos substantivos (o tipo de dado é conjunto para não repetir alternativas)
        while len(nouns_set) < 5:
            nouns_set.add(Game.get_random_noun())
        nouns_set = list(nouns_set)

        # Obtenção dos índices dos substantivos após sua adição
        for noun in nouns_set:
            nouns_translations.append(all_nouns_translations[all_nouns.index(noun)])

        # Substantivos salvos
        self.__nouns = nouns_set
        self.__nouns_tr = nouns_translations

        # Ir a próxima função
        Game.set_target_noun(self)

    # Salvar a alternativa certa
    def set_target_noun(self):
        # Substantivo da pergunta (último índice)
        self.__chosen_noun = self.__nouns[-1]
        self.__chosen_noun_translation = self.__nouns_tr[-1]
        # Ir a próxima função (perguntar ao usuário a resposta)
        Game.provide_alternative(self)

    def provide_alternative(self):
        shuffle(self.__nouns_tr)

        # Receberá o resultado da análise da resposta
        user_guess = []

        # Análise
        conditions = {
            'a': self.__nouns_tr[0] == self.__chosen_noun_translation,
            'b': self.__nouns_tr[1] == self.__chosen_noun_translation,
            'c': self.__nouns_tr[2] == self.__chosen_noun_translation,
            'd': self.__nouns_tr[3] == self.__chosen_noun_translation,
            'e': self.__nouns_tr[4] == self.__chosen_noun_translation,
        }

        # Menu
        print(ink(question_which_noun.format(closure_hint, ink(self.__chosen_noun), *self.__nouns_tr)))

        # Pedir alternativa
        self.__letter = input(hint)

        # Alternativa deve ser congruente com as instruções
        if self.__letter in right_menu_letters:

            # Verificação da alternativa
            for key in conditions:
                if self.__letter == key:
                    # Coletagem da resposta (a que for True)
                    user_guess.append(conditions[key])

            # Resposta certa, aumentar score, informar resultado e reiniciar
            if user_guess[0]:
                self.__score_plus += 1
                code_block_init('\n', terminal, success)
                print(current_score.format(ink(str(self.__score_plus)), ink(str(self.__score_minus))))
                Game.init_config(self)

            # Resposta incorreta, aumentar score negativo, informar resultado e reiniciar
            else:
                self.__score_minus += 1
                code_block_init('\n', terminal, failure)
                print(current_score.format(ink(str(self.__score_plus)), ink(str(self.__score_minus))))
                Game.init_config(self)
                # print(f'Resposta correta: {self.__chosen_noun_translation}')

        # Sair pelo menu principal
        if self.__letter == '0':
            code_block_init(terminal, thank_you_for_playing)
            exit(0)

        # Alternativa incongruente
        else:
            code_block_init(terminal, allowed_alternatives)
            # Repetir o pedido da alternativa
            Game.provide_alternative(self)

        # while loop_counter < menu_length:
        #     if self.__letter == right_menu_letters[loop_counter]:
        #         if self.__nouns_tr[loop_counter] == self.__chosen_noun_translation:
        #             code_block_init(terminal, success)
        #             Game.get_menu_options(self)
        #         else:
        #             code_block_init(terminal, failure)
        #             Game.get_menu_options(self)
        #     else:
        #         print(f'Opções são: {ink("a, b, c, d ou e")}')
        #         Game.provide_alternative(self)

    def __init__(self):
        self.__nouns = None
        self.__nouns_tr = None
        self.__chosen_noun = None
        self.__chosen_noun_translation = None
        self.__letter = None  # input
        self.__score_plus = 0
        self.__score_minus = 0


if __name__ == '__main__':
    test_object = Game()
    # print(test_object.get_nouns_from_source())
    # print(test_object.get_nouns_translation_from_source())

    # "ALGORITMO COMEÇA AQUI"
    test_object.init_config()
