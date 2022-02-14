

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Nouns(Base):

    # # Criação do arquivo do banco
    # @staticmethod
    # def database_config(name):
    #     import sqlalchemy
    #     engine = sqlalchemy.create_engine(f"sqlite:///{name}")
    #     return engine
    #
    # # Criação do executável de ações do banco
    # @staticmethod
    # def database_cursor(engine_var):
    #     from sqlalchemy.orm import sessionmaker
    #     Session = sessionmaker(bind=engine_var)
    #     cursor = Session()
    #     return cursor
    #
    # # Criação do banco (vars dos métodos gerenciadores criadas no pacote menu)
    # @staticmethod
    # def database_init(engine_var):
    #     Base.metadata.create_all(engine_var)
    #
    # # Gerenciar um objeto da classe e converter este para formato json (pk não incluso)
    # @staticmethod
    # def json(the_object):
    #     # nome do atributo do modelo: objeto externo.seu atributo
    #     return {
    #         "id_": the_object.id_,
    #         "noun": the_object.noun,
    #         "noun_tr": the_object.noun_tr
    #     }
    #
    # # Visualizar banco, armazenado em uma var e retornado
    # @staticmethod
    # def database_as_var(exec_):
    #     box = []  # armazenar o banco
    #     for content in exec_.query(Nouns).order_by(Nouns.id_):  # cursor consulta o banco e adquiri dados via pk
    #         box.append(Nouns.json(the_object=content))  # dados no cursor copiados, formatados em json
    #     return box
    #
    # # Função GET - verificação
    # @staticmethod
    # def database_query_by_noun(exec_, noun):
    #     # Cursor consulta o banco por um método específico que recebe uma chave: retorna objeto de memória ou None
    #     query_noun = exec_.query(Nouns).filter_by(noun=noun).first()
    #     if query_noun:  # Se objeto de memória, converter para json e retornar, senão retornar None
    #         query_noun_as_dict = Nouns.json(the_object=query_noun)
    #         return query_noun_as_dict
    #     return None
    #
    # # Função GET - verificação
    # @staticmethod
    # def database_query_by_noun_tr(exec_, noun_tr):
    #     # Cursor consulta o banco por um atributo específico: retorna objeto de memória ou None
    #     query_noun_tr = exec_.query(Nouns).filter_by(noun_tr=noun_tr).first()
    #     if query_noun_tr:  # Se objeto de memória, converter para json e retornar, senão retornar None
    #         query_noun_tr_as_dict = Nouns.json(the_object=query_noun_tr)
    #         return query_noun_tr_as_dict
    #     return None
    #
    # # Função PUT - necessário um objeto para funcionar
    # @staticmethod
    # def database_insert(exec_, noun_object):
    #     yes = None  # Se for alterada, o objeto não será add ao banco
    #     nouns_database = Nouns.database_as_var(exec_)  # Banco em var
    #     # Iteração sob o banco, para saber se um atributo do objeto está entre as chaves do banco
    #     for json in nouns_database:  # Iteração sob o banco
    #         if json['noun'] == noun_object.noun:  # nome do substantivo do banco == substantivo do objeto
    #             yes = True
    #     if not yes:  # Se não for: adicionar este objeto ao banco
    #         exec_.add(noun_object)
    #         exec_.commit()
    #
    # # Função PUT - necessária duas listas, uma para o substantivo e outra para a sua tradução
    # @staticmethod
    # def database_insert_many(exec_, length, noun_box, noun_tr_box):
    #     index = 0
    #     yes = None  # Se for alterada, o objeto não será add ao banco
    #     nouns_database = Nouns.database_as_var(exec_)  # Banco em var
    #
    #     while index < length:  # Loop para iterar sob todos os dados das listas
    #         noun_object = Nouns(noun=noun_box[index], noun_tr=noun_tr_box[index])  # objeto parâmetro
    #         for json in nouns_database:  # Iteração sob o banco
    #             if json['noun'] == noun_object.noun:  # nome do substantivo do banco == substantivo do objeto
    #                 yes = True
    #         if not yes:  # Se não for: adicionar este objeto ao banco
    #             exec_.add(noun_object)
    #             exec_.commit()
    #         index += 1
    #
    # @staticmethod
    # def object_noun_update(exec_, noun, _key, _value):
    #     object_update = '\n======= ATUALIZAÇÃO DO OBJETO ======='
    #     _before = '======= ANTES =======\n'
    #     _after = '======= DEPOIS =======\n'
    #
    #     target_object_then = Nouns.database_query_by_noun(exec_=exec_, noun=noun)
    #     exec_.query(Nouns).filter(Nouns.noun == noun).update({_key: _value})
    #     exec_.commit()
    #     target_object_now = Nouns.database_query_by_noun(exec_=exec_, noun=_value)
    #     print(object_update)
    #     print(_before, target_object_then)
    #     print(_after, target_object_now)
    #
    # @staticmethod
    # def object_noun_tr_update(exec_, noun_tr, _key, _value):
    #     object_update = '\n======= ATUALIZAÇÃO DO OBJETO ======='
    #     _before = '======= ANTES =======\n'
    #     _after = '======= DEPOIS =======\n'
    #
    #     target_object_then = Nouns.database_query_by_noun_tr(exec_=exec_, noun_tr=noun_tr)
    #     exec_.query(Nouns).filter(Nouns.noun_tr == noun_tr).update({_key: _value})
    #     exec_.commit()
    #     target_object_now = Nouns.database_query_by_noun_tr(exec_=exec_, noun_tr=_value)
    #     print(object_update)
    #     print(_before, target_object_then)
    #     print(_after, target_object_now)
    #
    # @staticmethod
    # def object_noun_delete(exec_, noun):
    #     object_deleted = '\n======= OBJETO DELETADO ======='
    #     object_to_be_deleted = Nouns.database_query_by_noun(exec_=exec_, noun=noun)  # objeto de memória ou None
    #     exec_.query(Nouns).filter(Nouns.noun == noun).delete()
    #     exec_.commit()
    #     print(object_deleted)
    #     print(object_to_be_deleted, '\n')

    __tablename__ = 'substantivos'

    id_ = Column(Integer, primary_key=True, autoincrement=True)
    verb = Column(String(100))                             # to try
    verb_translation = Column(String(100))                 # tentar
    verb_type = Column(String(100))                        # irregular
    "PASSADO SIMPLES"
    verb_past = Column(String(100))                        # tried
    verb_past_not = Column(String(100))                    # did not try
    verb_past_not_short = Column(String(100))              # didn't try
    "PRESENTE SIMPLES"
    verb_present = Column(String(100))                     # try
    verb_present_singular_not = Column(String(100))        # does not try
    verb_present_singular_not_short = Column(String(100))  # doesn't try
    verb_present_plural_not_ = Column(String(100))         # do not try
    verb_present_plural_not_short = Column(String(100))    # don't try
    "FUTURO SIMPLES"
    verb_future = Column(String(100))                      # will try
    verb_future_not = Column(String(100))                  # not try
    verb_future_not_short = Column(String(100))            # won't try
    "PASSADO CONTÍNUO"
    verb_past_continuous_singular = Column(String(100))            # was trying
    verb_past_continuous_plural = Column(String(100))              # were trying
    verb_past_continuous_singular_not = Column(String(100))        # was not trying
    verb_past_continuous_singular_not_short = Column(String(100))  # wasn't trying
    verb_past_continuous_plural_not = Column(String(100))          # were not trying
    verb_past_continuous_plural_not_short = Column(String(100))    # weren't trying
    "PRESENTE CONTÍNUO"
    verb_present_continuous_singular = Column(String(100))            # is trying
    verb_present_continuous_singular_not = Column(String(100))        # is not trying
    verb_present_continuous_singular_not_short = Column(String(100))  # isn't trying
    verb_present_continuous_plural = Column(String(100))              # are trying
    verb_present_continuous_plural_not = Column(String(100))          # are not trying
    verb_present_continuous_plural_not_short = Column(String(100))    # aren't trying
    "FUTURO CONTÍNUO"
    verb_future_continuous = Column(String(100))            # will be trying
    verb_future_continuous_not = Column(String(100))        # will not be trying
    verb_future_continuous_not_short = Column(String(100))  # won't be trying
    "PASSADO PERFEITO"
    verb_past_perfect = Column(String(100))            # had tried
    verb_past_perfect_not = Column(String(100))        # had not tried
    verb_past_perfect_not_short = Column(String(100))  # hadn't tried
    "PRESENTE PERFEITO"
    verb_present_perfect_singular = Column(String(100))            # has tried
    verb_present_perfect_singular_not = Column(String(100))        # has not tried
    verb_present_perfect_singular_not_short = Column(String(100))  # hasn't tried
    verb_present_perfect_plural = Column(String(100))              # have tried
    verb_present_perfect_plural_not = Column(String(100))          # have not tried
    verb_present_perfect_plural_not_short = Column(String(100))    # haven't tried
    "FUTURO PERFEITO"
    verb_future_perfect = Column(String(100))            # will have tried
    verb_future_perfect_not = Column(String(100))        # will not have tried
    verb_future_perfect_not_short = Column(String(100))  # won't have tried
    "PASSADO PERFEITO CONTÍNUO"
    verb_past_perfect_continuous = Column(String(100))            # had been trying
    verb_past_perfect_continuous_not = Column(String(100))        # had not been trying
    verb_past_perfect_continuous_not_short = Column(String(100))  # hadn't been trying
    "PRESENTE PERFEITO CONTÍNUO"
    verb_present_perfect_continuous_singular = Column(String(100))            # has been trying
    verb_present_perfect_continuous_singular_not = Column(String(100))        # has not been trying
    verb_present_perfect_continuous_singular_not_short = Column(String(100))  # hasn't been trying
    verb_present_perfect_continuous_plural = Column(String(100))              # have been trying
    verb_present_perfect_continuous_plural_not = Column(String(100))          # have not been trying
    verb_present_perfect_continuous_plural_not_short = Column(String(100))    # haven't been trying
    "FUTURE PERFEITO CONTÍNUO"
    verb_future_perfect_continuous = Column(String(100))                      # will have been trying
    verb_future_perfect_continuous_not = Column(String(100))                  # will not have been trying
    verb_future_perfect_continuous_not_short = Column(String(100))            # won't have been trying

    "PRESENTE VERBO MODAL COULD"
    verb_modal_could_present = Column(String(100))            # could try
    verb_modal_could_present_not = Column(String(100))        # could not try
    verb_modal_could_present_not_short = Column(String(100))  # couldn't try
    "PRESENTE CONTÍNUO VERBO MODAL COULD"
    verb_modal_could_present_continuous = Column(String(100))            # could be trying
    verb_modal_could_present_continuous_not = Column(String(100))        # could not be trying
    verb_modal_could_present_continuous_not_short = Column(String(100))  # couldn't be trying
    "PRESENTE PERFEITO VERBO MODAL COULD"
    verb_modal_could_present_perfect = Column(String(100))            # could have tried
    verb_modal_could_present_perfect_not = Column(String(100))        # could not have tried
    verb_modal_could_present_perfect_not_short = Column(String(100))  # couldn't have tried
    "PRESENTE PERFEITO CONTÍNUO VERBO MODAL COULD"
    verb_modal_could_present_perfect_continuous = Column(String(100))            # could have been trying
    verb_modal_could_present_perfect_continuous_not = Column(String(100))        # could not have been trying
    verb_modal_could_present_perfect_continuous_not_short = Column(String(100))  # couldn't have been trying

    "PRESENTE VERBO AUXILIAR SHOULD"
    verb_auxiliary_should = Column(String(100))                               # should try
    verb_auxiliary_should_not = Column(String(100))                           # should not try
    verb_auxiliary_should_not_short = Column(String(100))                     # shouldn't try
    "PRESENTE CONTÍNUO VERBO AUXILIAR SHOULD"
    verb_auxiliary_should_present_continuous = Column(String(100))            # should be trying
    verb_auxiliary_should_present_continuous_not = Column(String(100))        # should not be trying
    verb_auxiliary_should_present_continuous_not_short = Column(String(100))  # shouldn't be trying
    "PRESENTE PERFEITO VERBO AUXILIAR SHOULD"
    verb_auxiliary_should_present_perfect = Column(String(100))               # should have tried
    verb_auxiliary_should_present_perfect_not = Column(String(100))           # should not have tried
    verb_auxiliary_should_present_perfect_not_short = Column(String(100))     # shouldn't have tried
    "PRESENTE PERFEITO CONTÍNUO VERBO AUXILIAR SHOULD"
    verb_auxiliary_should_present_perfect_continuous_ = Column(String(100))           # should have been trying
    verb_auxiliary_should_present_perfect_continuous_not = Column(String(100))        # should not have been trying
    verb_auxiliary_should_present_perfect_continuous_not_short = Column(String(100))  # shouldn't have been trying

    "PRESENTE CONDICIONAL WOULD"
    verb_conditional_would_present = Column(String(100))            # would try
    verb_conditional_would_present_not = Column(String(100))        # would not try
    verb_conditional_would_present_not_short = Column(String(100))  # wouldn't try
    "PRESENTE CONTÍNUO CONDICIONAL WOULD"
    verb_conditional_would_present_continuous = Column(String(100))            # would be trying
    verb_conditional_would_present_continuous_not = Column(String(100))        # would not be trying
    verb_conditional_would_present_continuous_not_short = Column(String(100))  # wouldn't be trying
    "PRESENTE PERFEITO CONDICIONAL WOULD"
    verb_conditional_would_present_perfect = Column(String(100))            # would have tried
    verb_conditional_would_present_perfect_not = Column(String(100))        # would not have tried
    verb_conditional_would_present_perfect_not_short = Column(String(100))  # wouldn't have tried
    "PRESENTE PERFEITO CONTÍNUO CONDICIONAL WOULD"
    verb_conditional_would_present_perfect_continuous = Column(String(100))            # would have been trying
    verb_conditional_would_present_perfect_continuous_not = Column(String(100))        # would not have been trying
    verb_conditional_would_present_perfect_continuous_not_short = Column(String(100))  # wouldn't have been trying
