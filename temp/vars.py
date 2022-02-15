

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
    'ar', 'ares', 'área', 'áreas', 'arte', 'artes', 'corpo', 'corpos', 'livro', 'livros', 'negócios', 'os negócios',
    'carro ', 'carros', 'mudança', 'mudanças', 'criança', 'crianças', 'cidade', 'cidades',

    'comunidade', 'comunidades', 'empresa', 'empresas', 'país', 'países', 'dia', 'dias', 'porta', 'portas',
    'final', 'finais', 'olho', 'olhos', 'rosto', 'rostos', 'fato', 'fatos', 'família', 'famílias',

    'pai', 'pais', 'força', 'forças', 'amigo', 'amigos', 'jogo', 'jogos', 'menina', 'meninas', 'governo', 'governos',
    'grupo', 'grupos', 'cara', 'pessoal', 'mão', 'mãos', 'cabeça', 'cabeças',

    'história', 'histórias', 'casa', 'casas', 'hora', 'horas', 'casa', 'casas', 'ideia', 'ideias',
    'problema', 'problemas', 'emprego', 'empregos', 'criança', 'crianças', 'tipo', 'tipos', 'lei', 'leis',


    'nível', 'níveis', 'vida', 'vidas', 'linha', 'linhas', 'homem', 'homens', 'membro', 'membros ', 'minuto', 'minutos',
    'momento', 'momentos', 'mês', 'meses', 'manhã', 'manhãs', 'mãe', 'mães',

    'nome', 'nomes', 'noite', 'noites', 'número', 'números', 'escritório', 'escritórios', 'outro(a)', 'outros(as)',
    'pai', 'pais', 'parte', 'partes', 'festa', 'festas', 'pessoa', 'pessoas', 'pedaço de informação', 'pedaços de informação',

    'lugar', 'lugares', 'ponto', 'pontos', 'poder', 'poderes', 'presidente', 'presidentes', 'problema', 'problemas',
    'programa', 'programas', 'questão', 'questões', 'razão', 'razões', 'pesquisa', 'pesquisas', 'resultado', 'resultados',

    'direito', 'direitos', 'quarto', 'quartos', 'escola', 'escolas', 'serviço', 'serviços', 'lado', 'lados',
    'estado', 'estados', 'história', 'histórias', 'estudante', 'estudantes', 'estudo', 'estudos', 'sistema', 'sistemas',

    'professor(a)', 'professores', 'equipe', 'equipes', 'coisa', 'coisas', 'tempo', 'tempos', 'guerra', 'guerras',
    'água', 'águas', 'caminho', 'caminhos', 'semana', 'semanas', 'mulher', 'mulheres', 'palavra', 'palavras',

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
    'fresco / legal', 'novo(a)', 'bom(a)', 'alto(a) (não humano)', 'velho(a)', 'ótimo(a)', 'grande', 'pequeno(a)',
    'grande', 'amplo / grande', 'jovem / novo(a)', 'diferente', 'persistente', 'longo', 'pequeno', 'importante',
    'atraente / tentador(a)', 'ruim / mau / má', 'persistente / tenaz', 'invisível',

    'real', 'certo / correto', 'liso / plano', 'único(a)', 'público', 'certo / seguro', 'baixo(a)', 'cedo / inicial',
    'magro(a)', 'humano(a)', 'sadio / saudável', 'doente / doentio / insalubre', 'difícil / duro(a)', 'doente',
    'melhor', 'sujo(a)', 'forte', 'possível', 'sonolento', 'hábil / habilidoso',

    'gratuito(a) / livre', 'nojento / repugnante', 'verdadeiro(a)', 'escondido(a) / oculto(a)', 'manchado(a)',
    'cheio / completo', 'especial', 'fácil', 'claro / evidente', 'confortável', 'desagradável / nojento(a)',
    'desagradável', 'aberto(a)', 'desesperado(a)', 'difícil', 'disponível', 'provável', 'baixo(a) / curto(a)',
    'solteiro(a) / único(a)', 'de cabeça para baixo',

    'incomparável', 'errado(a)', 'privado(a)', 'brilhante', 'estrangeiro(a)', 'bom(a) / excelente', 'comum', 'pobre',
    'natural', 'significativo', 'semelhante / similar / parecido', 'quente', 'morto(a)', 'demente', 'feliz', 'sério(a)',
    'pronto(a)', 'simples', 'escondido(a)', 'despreocupado(a) / desinteressado(a) / indiferente',

    'silencioso(a)', 'surpreendente', 'perfeito', 'lento(a)', 'democrático(a)', 'escuro(a)', 'temporário(a)',
    'provisório(a)', 'perto / próximo(a)', 'forte / pesado', 'religioso(a)', 'frio(a)', 'aliviado(a)', 'principal',
    'insistente', 'legal', 'enorme', 'famoso(a)', 'tradicional', 'divorciado(a)',

    'estúpido', 'irrelevante', 'doce', 'com raiva / irritado(a) / zangado(a)', 'ambicioso(a)', 'indiferente',
    'maravilhoso(a)', 'idêntico(a)', 'esperto(a) / inteligente', 'entusiasmado(a)', 'vibrante', 'afirmativo(a)',
    'negativo', 'compreensivo(a)', 'intuitivo(a)', 'estranho(a)', 'estranho(a)', 'ímpar / estranho(a) / esquisito(a)',
    'digno(a)', 'flexível',

    'detestável', 'ligeiro(a) / rápido(a)', 'casado(a)', 'fechado(a)', 'interessante', 'interesado(a)', 'sórdido / vil',
    'obcecado(a)', 'cauteloso(a)', 'prudente', 'alto / barulhento(a)'
]

# print(len(nouns))
# print(len(nouns_pt_br))
# print(len(adjectives))
# print(len(adjectives_pt_br))
# print(adjectives[29])
# print(adjectives_pt_br[29])
