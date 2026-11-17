# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/prebattle_highlights/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
FEATURE = 'prebattle_highlights'

class PrebattleHighlightsLogAction(Enum):
    VIEWED = 'viewed'
    COLLAPSE = 'collapse'

class PrebattleHighlightsLogKeys(Enum):
    PBH = 'pbh'
    PBH_OUT_OF_FOCUS = 'pbh_out_of_focus'
    FULLY_VIEWED = 'fully_viewed'
    ESC = 'esc'
    SETTINGS_PBH = 'settings_pbh'
    SETTINGS_HISTORICAL = 'settings_historical'
    NOT_ENOUGH_TIME = 'not_enough_time'
