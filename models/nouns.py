

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Nouns(Base):

    # Criação do arquivo do banco
    @staticmethod
    def database_config(name):
        import sqlalchemy
        engine = sqlalchemy.create_engine(f"sqlite:///{name}")
        return engine

    # Criação do executável de ações do banco
    @staticmethod
    def database_cursor(engine_var):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=engine_var)
        cursor = Session()
        return cursor

    # Criação do banco
    @staticmethod
    def database_init(engine_var):
        Base.metadata.create_all(engine_var)

    # Gerenciar um objeto da classe e converter este para formato json (pk não incluso)
    @staticmethod
    def json(the_object):
        # nome do atributo do modelo: objeto externo.seu atributo
        return {
            "id_": the_object.id_,
            "noun": the_object.noun,
            "noun_translation": the_object.noun_translation,
            "noun_plural": the_object.noun_plural,
            "noun_plural_translation": the_object.noun_plural_translation,
        }

    # Visualizar banco, armazenado em uma var e retornado
    @staticmethod
    def database_as_var(exec_):
        box = []  # armazenar o banco
        for content in exec_.query(Nouns).order_by(Nouns.id_):  # cursor consulta o banco e adquiri dados via pk
            box.append(Nouns.json(the_object=content))  # dados no cursor copiados, formatados em json
        return box

    # Função GET - verificação
    @staticmethod
    def database_query_by_noun(exec_, noun):
        # Cursor consulta o banco por um método específico que recebe uma chave: retorna objeto de memória ou None
        query_noun = exec_.query(Nouns).filter_by(noun=noun).first()
        if query_noun:  # Se objeto de memória, converter para json e retornar, senão retornar None
            query_noun_as_dict = Nouns.json(the_object=query_noun)
            return query_noun_as_dict
        return None

    # Função GET - verificação
    @staticmethod
    def database_query_by_noun_tr(exec_, noun_tr):
        # Cursor consulta o banco por um atributo específico: retorna objeto de memória ou None
        query_noun_tr = exec_.query(Nouns).filter_by(noun_tr=noun_tr).first()
        if query_noun_tr:  # Se objeto de memória, converter para json e retornar, senão retornar None
            query_noun_tr_as_dict = Nouns.json(the_object=query_noun_tr)
            return query_noun_tr_as_dict
        return None

    # Função PUT - necessário um objeto para funcionar
    @staticmethod
    def database_insert(exec_, noun_object):
        yes = None  # Se for alterada, o objeto não será add ao banco
        nouns_database = Nouns.database_as_var(exec_)  # Banco em var
        # Iteração sob o banco, para saber se um atributo do objeto está entre as chaves do banco
        for json in nouns_database:  # Iteração sob o banco
            if json['noun'] == noun_object.noun:  # nome do substantivo do banco == substantivo do objeto
                yes = True
        if not yes:  # Se não for: adicionar este objeto ao banco
            exec_.add(noun_object)
            exec_.commit()

    # Função PUT - necessária duas listas, uma para o substantivo e outra para a sua tradução
    @staticmethod
    def database_insert_many(exec_, length, box_noun, box_noun_translation, box_noun_plural, box_noun_plural_translation):
        # noun = Column(String(100))
        #     noun_translation = Column(String(100))
        #     noun_plural = Column(String(100))
        #     noun_plural_translation = Column(String(100))
        index = 0
        yes = None  # Se for alterada, o objeto não será add ao banco
        nouns_database = Nouns.database_as_var(exec_)  # Banco em var

        while index < length:  # Loop para iterar sob todos os dados das listas
            noun_object = Nouns(noun=box_noun[index],
                                noun_translation=box_noun_translation[index],
                                noun_plural=box_noun_plural[index],
                                noun_plural_translation=box_noun_plural_translation[index],
            )  # objeto parâmetro
            for json in nouns_database:  # Iteração sob o banco
                if json['noun'] == noun_object.noun:  # nome do substantivo do banco == substantivo do objeto
                    yes = True
            if not yes:  # Se não for: adicionar este objeto ao banco
                exec_.add(noun_object)
                exec_.commit()
            index += 1

    @staticmethod
    def object_noun_update(exec_, noun, _key, _value):
        object_update = '\n======= ATUALIZAÇÃO DO OBJETO ======='
        _before = '======= ANTES =======\n'
        _after = '======= DEPOIS =======\n'

        target_object_then = Nouns.database_query_by_noun(exec_=exec_, noun=noun)
        exec_.query(Nouns).filter(Nouns.noun == noun).update({_key: _value})
        exec_.commit()
        target_object_now = Nouns.database_query_by_noun(exec_=exec_, noun=_value)
        print(object_update)
        print(_before, target_object_then)
        print(_after, target_object_now)

    @staticmethod
    def object_noun_translation_update(exec_, noun_tr, _key, _value):
        object_update = '\n======= ATUALIZAÇÃO DO OBJETO ======='
        _before = '======= ANTES =======\n'
        _after = '======= DEPOIS =======\n'

        target_object_then = Nouns.database_query_by_noun_tr(exec_=exec_, noun_tr=noun_tr)
        exec_.query(Nouns).filter(Nouns.noun_tr == noun_tr).update({_key: _value})
        exec_.commit()
        target_object_now = Nouns.database_query_by_noun_tr(exec_=exec_, noun_tr=_value)
        print(object_update)
        print(_before, target_object_then)
        print(_after, target_object_now)

    @staticmethod
    def object_noun_delete(exec_, noun):
        object_deleted = '\n======= OBJETO DELETADO ======='
        object_to_be_deleted = Nouns.database_query_by_noun(exec_=exec_, noun=noun)  # objeto de memória ou None
        exec_.query(Nouns).filter(Nouns.noun == noun).delete()
        exec_.commit()
        print(object_deleted)
        print(object_to_be_deleted, '\n')

    __tablename__ = 'substantivos'

    id_ = Column(Integer, primary_key=True, autoincrement=True)
    noun = Column(String(100))
    noun_translation = Column(String(100))
    noun_plural = Column(String(100))
    noun_plural_translation = Column(String(100))
