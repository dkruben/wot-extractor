# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
DEFAULT_LOGGER_NAME = 'UI_LOG'

class LogLevels(object):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30

class CommonLogActions(str, Enum):
    CLICK = 'click'
    KEYDOWN = 'keydown'

class InputLogActions(str, Enum):
    TRIGGERED = 'inputTriggered'
