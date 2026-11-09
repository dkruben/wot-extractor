# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/vehicle_hub/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
TIME_LIMIT = 2

class Features(str, Enum):
    ARMOR_INSPECTOR = 'armor_inspector'

class Tabs(str, Enum):
    ARMOR_TAB = 'armor_tab'

class LogItems(str, Enum):
    ARMOR_TOOLTIP = 'armor_tooltip'

class LogActions(str, Enum):
    OPEN = 'open'
    CLOSE = 'close'
    CLICK = 'click'
    TOOLTIP_ACTION = 'watched'
    EXPAND = 'expand'
    COLLAPSE = 'collapse'
