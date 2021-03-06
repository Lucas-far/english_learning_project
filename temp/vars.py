

# nouns = [
#     'air', 'airs', 'area', 'areas', 'art', 'arts', 'body', 'bodies', 'book', 'books',
#     'business', 'businesses', 'car', 'cars', 'change', 'changes', 'child', 'children', 'city', 'cities',
#
#     'community', 'communities', 'company', 'companies', 'country', 'countries', 'day', 'days', 'door', 'doors',
#     'ending', 'endings', 'eye', 'eyes', 'face', 'faces', 'fact', 'facts', 'family', 'families',
#
#     'father', 'fathers', 'strength', 'strengths', 'friend', 'friends', 'game', 'games', 'girl', 'girls',
#     'government', 'governments', 'group', 'groups', 'guy', 'guys', 'hand', 'hands', 'head', 'heads',
#
#     'history', 'histories', 'home', 'homes', 'hour', 'hours', 'house', 'houses', 'idea', 'ideas',
#     'issue', 'issues', 'job', 'jobs', 'kid', 'kids', 'kind', 'kinds', 'law', 'laws',
#
#     'level', 'levels', 'life', 'lifes', 'line', 'lines', 'man', 'men', 'member', 'members',
#     'minute', 'minutes', 'moment', 'moments', 'month', 'months', 'morning', 'mornings', 'mother', 'mothers',
#
#     'name', 'names', 'night', 'nights', 'number', 'numbers', 'office', 'offices', 'other', 'others',
#     'parent', 'parents', 'part', 'parts', 'party', 'parties', 'person', 'people', 'piece of information', 'pieces of information',
#
#     'place', 'places', 'point', 'points', 'power', 'powers', 'president', 'presidents', 'problem', 'problems',
#     'program', 'programs', 'question', 'questions', 'reason', 'reasons', 'research', 'researches', 'result', 'results',
#
#     'right', 'rights', 'room', 'rooms', 'school', 'schools', 'service', 'services', 'side', 'sides',
#     'state', 'states', 'story', 'stories', 'student', 'students', 'study', 'studies', 'system', 'systems',
#
#     'teacher', 'teachers', 'team', 'teams', 'thing', 'things', 'time', 'times', 'war', 'wars',
#     'water', 'waters', 'way', 'ways', 'week', 'weeks', 'woman', 'women', 'word', 'words',
#
#     'work', 'works', 'world', 'worlds', 'year', 'years'
# ]

nouns = [
    'air', 'airs', 'area', 'areas', 'art', 'arts', 'body', 'bodies', 'book', 'books',
    'business', 'businesses', 'car', 'cars', 'change', 'changes', 'child', 'children', 'city', 'cities',

    'community', 'communities', 'company', 'companies', 'country', 'countries', 'day', 'days', 'door', 'doors',
    'ending', 'endings', 'eye', 'eyes', 'face', 'faces', 'fact', 'facts', 'family', 'families',

    'father', 'fathers', 'strength', 'strengths', 'friend', 'friends', 'game', 'games', 'girl', 'girls',
    'government', 'governments', 'group', 'groups', 'guy', 'guys', 'hand', 'hands', 'head', 'heads',

    'history', 'histories', 'home', 'homes', 'hour', 'hours', 'house', 'houses', 'idea', 'ideas',
    'issue', 'issues', 'job', 'jobs', 'kid', 'kids', 'kind', 'kinds', 'law', 'laws',

    'level', 'levels', 'life', 'lifes', 'line', 'lines', 'man', 'men', 'member', 'members',
    'minute', 'minutes', 'moment', 'moments', 'month', 'months', 'morning', 'mornings', 'mother', 'mothers',

    'name', 'names', 'night', 'nights', 'number', 'numbers', 'office', 'offices', 'other', 'others',
    'parent', 'parents', 'part', 'parts', 'party', 'parties', 'person', 'people', 'piece of information', 'pieces of information',

    'place', 'places', 'point', 'points', 'power', 'powers', 'president', 'presidents', 'problem', 'problems',
    'program', 'programs', 'question', 'questions', 'reason', 'reasons', 'research', 'researches', 'result', 'results',

    'right', 'rights', 'room', 'rooms', 'school', 'schools', 'service', 'services', 'side', 'sides',
    'state', 'states', 'story', 'stories', 'student', 'students', 'study', 'studies', 'system', 'systems',

    'teacher', 'teachers', 'team', 'teams', 'thing', 'things', 'time', 'times', 'war', 'wars',
    'water', 'waters', 'way', 'ways', 'week', 'weeks', 'woman', 'women', 'word', 'words',

    'work', 'works', 'world', 'worlds', 'year', 'years'
]
nouns_singular = []
nouns_plural = []

for data in nouns:
    the_index = nouns.index(data)
    if not the_index % 2:
        nouns_singular.append(nouns[the_index])
    else:
        nouns_plural.append(nouns[the_index])

# print(nouns_singular)
# print(nouns_plural)

nouns_pt_br = [
    'ar', 'ares', '??rea', '??reas', 'arte', 'artes', 'corpo', 'corpos', 'livro', 'livros', 'neg??cios', 'os neg??cios',
    'carro ', 'carros', 'mudan??a', 'mudan??as', 'crian??a', 'crian??as', 'cidade', 'cidades',

    'comunidade', 'comunidades', 'empresa', 'empresas', 'pa??s', 'pa??ses', 'dia', 'dias', 'porta', 'portas',
    'final', 'finais', 'olho', 'olhos', 'rosto', 'rostos', 'fato', 'fatos', 'fam??lia', 'fam??lias',

    'pai', 'pais', 'for??a', 'for??as', 'amigo', 'amigos', 'jogo', 'jogos', 'menina', 'meninas', 'governo', 'governos',
    'grupo', 'grupos', 'cara', 'pessoal', 'm??o', 'm??os', 'cabe??a', 'cabe??as',

    'hist??ria', 'hist??rias', 'casa', 'casas', 'hora', 'horas', 'casa', 'casas', 'ideia', 'ideias',
    'problema', 'problemas', 'emprego', 'empregos', 'crian??a', 'crian??as', 'tipo', 'tipos', 'lei', 'leis',


    'n??vel', 'n??veis', 'vida', 'vidas', 'linha', 'linhas', 'homem', 'homens', 'membro', 'membros ', 'minuto', 'minutos',
    'momento', 'momentos', 'm??s', 'meses', 'manh??', 'manh??s', 'm??e', 'm??es',

    'nome', 'nomes', 'noite', 'noites', 'n??mero', 'n??meros', 'escrit??rio', 'escrit??rios', 'outro(a)', 'outros(as)',
    'pai', 'pais', 'parte', 'partes', 'festa', 'festas', 'pessoa', 'pessoas', 'peda??o de informa????o', 'peda??os de informa????o',

    'lugar', 'lugares', 'ponto', 'pontos', 'poder', 'poderes', 'presidente', 'presidentes', 'problema', 'problemas',
    'programa', 'programas', 'quest??o', 'quest??es', 'raz??o', 'raz??es', 'pesquisa', 'pesquisas', 'resultado', 'resultados',

    'direito', 'direitos', 'quarto', 'quartos', 'escola', 'escolas', 'servi??o', 'servi??os', 'lado', 'lados',
    'estado', 'estados', 'hist??ria', 'hist??rias', 'estudante', 'estudantes', 'estudo', 'estudos', 'sistema', 'sistemas',

    'professor(a)', 'professores', 'equipe', 'equipes', 'coisa', 'coisas', 'tempo', 'tempos', 'guerra', 'guerras',
    '??gua', '??guas', 'caminho', 'caminhos', 'semana', 'semanas', 'mulher', 'mulheres', 'palavra', 'palavras',

    'trabalho', 'trabalhos', 'mundo', 'mundos', 'ano', 'anos'
]
nouns_singular_translation = []
nouns_plural_translation = []

for data in nouns_pt_br:
    the_index = nouns_pt_br.index(data)
    if not the_index % 2:
        nouns_singular_translation.append(nouns_pt_br[the_index])
    else:
        nouns_plural_translation.append(nouns_pt_br[the_index])

# print(nouns_singular_translation)
# print(nouns_plural_translation)

adjectives = [
    'cool', 'new', 'good', 'high', 'old', 'great', 'big', 'small', 'large', 'wide', 'young',
    'different', 'persistent', 'long', 'little', 'important', 'tempting', 'bad', 'tenacious', 'invisible',

    'real', 'right', 'flat', 'only', 'public', 'sure', 'low', 'early', 'skinny', 'human', 'healthy', 'unhealthy',
    'hard', 'sick', 'better', 'dirty', 'strong', 'possible', 'drowsy', 'skilled',

    'free', 'disgusting', 'true', 'hidden', 'spotted', 'full', 'special', 'easy', 'clear', 'comfortable', 'nasty',
    'unpleasant', 'open', 'desperate', 'difficult', 'available', 'likely', 'short', 'single', 'upside down',

    'incomparable', 'wrong', 'private', 'brilliant', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant',
    'similar', 'hot', 'dead', 'demented', 'happy', 'serious', 'ready', 'simple', 'concealed', 'unconcerned',

    'silent', 'astonishing', 'perfect', 'slow', 'democratic', 'dark', 'temporary', 'provisory', 'close', 'heavy',
    'religious', 'cold', 'relieved', 'main', 'insistent', 'nice', 'huge', 'famous', 'traditional', 'divorced',

    'stupid', 'irrelevant', 'sweet', 'angry', 'ambitious', 'indifferent', 'marvelous', 'identical', 'clever',
    'enthusiastic', 'vibrant', 'affirmative', 'negative', 'comprehensive', 'intuitive', 'strange', 'weird', 'odd',
    'worthy', 'flexible',

    'obnoxiously', 'fast', 'married', 'closed', 'interesting', 'interested', 'sordid', 'obsessed', 'cautious',
    'prudent', 'loud'
]

adjectives_pt_br = [
    'fresco / legal', 'novo(a)', 'bom(a)', 'alto(a) (n??o humano)', 'velho(a)', '??timo(a)', 'grande', 'pequeno(a)',
    'grande', 'amplo / grande', 'jovem / novo(a)', 'diferente', 'persistente', 'longo', 'pequeno', 'importante',
    'atraente / tentador(a)', 'ruim / mau / m??', 'persistente / tenaz', 'invis??vel',

    'real', 'certo / correto', 'liso / plano', '??nico(a)', 'p??blico', 'certo / seguro', 'baixo(a)', 'cedo / inicial',
    'magro(a)', 'humano(a)', 'sadio / saud??vel', 'doente / doentio / insalubre', 'dif??cil / duro(a)', 'doente',
    'melhor', 'sujo(a)', 'forte', 'poss??vel', 'sonolento', 'h??bil / habilidoso',

    'gratuito(a) / livre', 'nojento / repugnante', 'verdadeiro(a)', 'escondido(a) / oculto(a)', 'manchado(a)',
    'cheio / completo', 'especial', 'f??cil', 'claro / evidente', 'confort??vel', 'desagrad??vel / nojento(a)',
    'desagrad??vel', 'aberto(a)', 'desesperado(a)', 'dif??cil', 'dispon??vel', 'prov??vel', 'baixo(a) / curto(a)',
    'solteiro(a) / ??nico(a)', 'de cabe??a para baixo',

    'incompar??vel', 'errado(a)', 'privado(a)', 'brilhante', 'estrangeiro(a)', 'bom(a) / excelente', 'comum', 'pobre',
    'natural', 'significativo', 'semelhante / similar / parecido', 'quente', 'morto(a)', 'demente', 'feliz', 's??rio(a)',
    'pronto(a)', 'simples', 'escondido(a)', 'despreocupado(a) / desinteressado(a) / indiferente',

    'silencioso(a)', 'surpreendente', 'perfeito', 'lento(a)', 'democr??tico(a)', 'escuro(a)', 'tempor??rio(a)',
    'provis??rio(a)', 'perto / pr??ximo(a)', 'forte / pesado', 'religioso(a)', 'frio(a)', 'aliviado(a)', 'principal',
    'insistente', 'legal', 'enorme', 'famoso(a)', 'tradicional', 'divorciado(a)',

    'est??pido', 'irrelevante', 'doce', 'com raiva / irritado(a) / zangado(a)', 'ambicioso(a)', 'indiferente',
    'maravilhoso(a)', 'id??ntico(a)', 'esperto(a) / inteligente', 'entusiasmado(a)', 'vibrante', 'afirmativo(a)',
    'negativo', 'compreensivo(a)', 'intuitivo(a)', 'estranho(a)', 'estranho(a)', '??mpar / estranho(a) / esquisito(a)',
    'digno(a)', 'flex??vel',

    'detest??vel', 'ligeiro(a) / r??pido(a)', 'casado(a)', 'fechado(a)', 'interessante', 'interesado(a)', 's??rdido / vil',
    'obcecado(a)', 'cauteloso(a)', 'prudente', 'alto / barulhento(a)'
]

# print(len(nouns))
# print(len(nouns_pt_br))
# print(len(adjectives))
# print(len(adjectives_pt_br))
# print(adjectives[29])
# print(adjectives_pt_br[29])
