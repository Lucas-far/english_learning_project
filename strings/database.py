

from functions.database import ink

hint = ink('\nDigite após a seta e aperte ENTER ---> ')

object_search_label = ink('\n====== PESQUISA DE {} ======')
object_add_label = ink('\n======= ADIÇÃO DE {} =======')
object_edit_label = ink('\n======= EDIÇÃO DE {} =======')
object_delete_label = ink('\n======= REMOÇÃO DO {} =======')
session_end = f'Encerrar sessão (Digitar 0)'
session_start = '{} (Digitar 1)'

input_text_operation = f'\nQual operação acima deseja realizar? {ink(hint)}'
input_text_noun = f'\nInforme o nome do substantivo {ink(hint)}'
input_text_noun_tr = f'\nInforme a tradução do substantivo {ink(hint)}'

closure = 'Sessão encerrada. Volte sempre que precisar!\n'
terminal = ink('======= TERMINAL =======')
options = ink('======= OPÇÕES DE MENU =======')
error = ink('\n========== MENSAGEM DE ERRO ==========')
warn = 'As opções de menu vão de {} até {}.\n'
roll = 'Pressione ENTER para continuar.\n'

invalid_data = '{} é um texto. Você precisa fornecer algum texto que o represente.\n'

noun_object_repeated = 'O substantivo "{}" já existe. Sua adição ao banco foi cancelada.'
noun_object_added = 'Substantivo adicionado: {}'

label_find_success = ink('\n======= {} ENCONTRADO =======')
label_find_failure = "Substantivo '{}' não foi encontrado"

not_found = 'O {} "{}" não foi encontrado.'
attempts_remaining = 'Tentativas restantes: {}'
attempts_exceeded = 'Número de tentativas máxima excedida: {}'
attempts_show = 'Tentativas restantes: {}'
search_in_the_database = 'Consulte o banco.\n'

edit_element = 'Atualizar {} (digite 1)'
edit_element_tr = 'Atualizar a tradução do {} (digite 2)'
edit_both = 'Atualizar ambos (digite 3)'

chosen_option = '\nOpção escolhida: {}'
new_value = '\nInforme o novo valor para {} {}'
options_one_to_three = f'\nEscolha uma das opções acima (entre 1 a 3) {hint}'

empty_database = 'Banco de dados vazio. Insira um objeto.'
noun_to_be_deleted = f'\nQual o nome do substanto a ser deletado? {ink(hint)}'
ask_if_remove = f'Confirmar a remoção? (0 = não deletar) (1 = deletar) {ink(hint)}'
object_removal_canceled = 'Remoção do objeto cancelada.\n'

closure_hint = ink('digite 0 e aperte ENTER')
question_which_noun = """
SAIR: {}
======= QUAL O SIGNIFICADO DO SUBSTANTIVO {}? =======
a) {}
b) {}
c) {}
d) {}
e) {} """

success = 'Resposta correta'
failure = 'Resposta incorreta'
allowed_alternatives = 'Alternativas válidas: a, b, c, d ou e'
thank_you_for_playing = 'Obrigado por jogar. Volte sempre!'

current_score = """
==================== PLACAR ====================
Corretas {} x {} Erradas """
