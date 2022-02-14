

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Adjectives(Base):

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

    # Criação do banco (vars dos métodos gerenciadores criadas no pacote menu)
    @staticmethod
    def database_init(engine_var):
        Base.metadata.create_all(engine_var)

    # Gerenciar um objeto da classe e converter este para formato json (pk não incluso)
    @staticmethod
    def json(the_object):
        # nome do atributo do modelo: objeto externo.seu atributo
        return {
            "id_": the_object.id_,
            "adjective": the_object.adjective,
            "adjective_tr": the_object.adjective_tr
        }

    # Visualizar banco, armazenado em uma var e retornado
    @staticmethod
    def database_as_var(exec_):
        box = []  # armazenar o banco
        for content in exec_.query(Adjectives).order_by(Adjectives.id_):  # cursor consulta o banco e adquiri dados via pk
            box.append(Adjectives.json(the_object=content))  # dados no cursor copiados, formatados em json
        return box

    # Função GET - verificação
    @staticmethod
    def database_query_by_adjective(exec_, adjective):
        # Cursor consulta o banco por um atributo específico: retorna objeto de memória ou None
        query_adjective = exec_.query(Adjectives).filter_by(adjective=adjective).first()
        if query_adjective:  # Se objeto de memória, converter para json e retornar, senão retornar None
            query_adjective_as_dict = Adjectives.json(the_object=query_adjective)
            return query_adjective_as_dict
        return None

    # Função PUT - necessário um objeto para funcionar
    @staticmethod
    def database_insert(exec_, adjective_object):
        yes = None  # Se for alterada, o objeto não será add ao banco
        adjectives_database = Adjectives.database_as_var(exec_)  # Banco em var
        # Iteração sob o banco, para saber se um atributo do objeto está entre as chaves do banco
        for json in adjectives_database:  # Iteração sob o banco
            if json['adjective'] == adjective_object.adjective:  # nome do substantivo do banco == substantivo do objeto
                yes = True
        if not yes:  # Se não for: adicionar este objeto ao banco
            exec_.add(adjective_object)
            exec_.commit()

    # Função PUT - necessária duas listas, uma para o substantivo e outra para a sua tradução
    @staticmethod
    def database_insert_many(exec_, length, adjective_box, adjective_tr_box):
        index = 0
        yes = None  # Se for alterada, o objeto não será add ao banco
        adjectives_database = Adjectives.database_as_var(exec_)  # Banco em var

        while index < length:  # Loop para iterar sob todos os dados das listas
            adjective_object = Adjectives(adjective=adjective_box[index], adjective_tr=adjective_tr_box[index])  # objeto parâmetro
            for json in adjectives_database:  # Iteração sob o banco
                if json['noun'] == adjective_object.adjective:  # nome do substantivo do banco == substantivo do objeto
                    yes = True
            if not yes:  # Se não for: adicionar este objeto ao banco
                exec_.add(adjective_object)
                exec_.commit()
            index += 1

    __tablename__ = 'adjetivos'

    id_ = Column(Integer, primary_key=True, autoincrement=True)
    adjective = Column(String(100))
    adjective_tr = Column(String(100))
