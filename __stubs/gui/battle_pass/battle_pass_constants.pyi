# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/battle_pass_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, unique as unique
MIN_LEVEL = 1

class BonusesLayoutConsts(object):
    PRIORITY_KEY = 'priority'
    VISIBILITY_KEY = 'isVisible'
    OVERRIDE_KEY = 'override'
    ID_KEY = 'id'
    LEVEL_KEY = 'level'
    BIG_ICON_KEY = 'bigIcon'
    RARITY = 'rarity'
    MAIN_KEYS: tuple
    INT_VALUES: tuple
    BOOL_VALUES: tuple

# decorador original: @unique
class ChapterState(Enum):
    ACTIVE = 'active'
    PAUSED = 'paused'
    COMPLETED = 'completed'
    NOT_STARTED = 'notStarted'
