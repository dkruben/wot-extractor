# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/ingame_tournament_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum

class IngameTournamentType(Enum):
    WCI = 'wci'
    OLS = 'ols'

class IngameTournamentState(Enum):
    INTRO = 'tournament_intro'
    IN_PROGRESS = 'tournament_in_live'
    BETWEEN_SHOWMATCHES = 'tournament_between_showmatch_days'
    FINISHED = 'tournament_finished'

class IngameTournamentBracketType(Enum):
    RR = 'RR'
    DE = 'DE'

class IngameTournamentMatchState(Enum):
    UPCOMING = 'upcoming'
    IN_LIVE = 'in_live'
    COMPLETED = 'completed'

class IngameTournamentUrlType(Enum):
    YOUTUBE = 'youtube'
    TWITCH = 'twitch'
    DOUYIN = 'douyin'
    HUYA = 'huya'

class IngameTournamentLogoSize(Enum):
    SMALL = '48x48'
    MEDIUM = '86x86'
    LARGE = '260x260'
    EXTRA_LARGE = '522x522'
