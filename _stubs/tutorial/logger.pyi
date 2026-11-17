# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import _doLog as _doLog, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
CURRENT_LOG_LEVEL = LOG_LEVEL.ERROR
__all__: tuple

class LOG_LEVEL(object):
    ERROR = 1
    WARNING = 2
    DEBUG = 4
    MEMORY = 8
    REQUEST = 16

def LOG_DEBUG(msg, *args):
    ...
def LOG_WARNING(msg, *args):
    ...
def LOG_ERROR(msg, *args):
    ...
def LOG_MEMORY(msg, *args):
    ...
def LOG_REQUEST(msg, *args):
    ...
