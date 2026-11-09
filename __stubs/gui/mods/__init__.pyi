# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/mods/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import importlib as importlib
import string as string
import ResMgr as ResMgr
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_WARNING as LOG_WARNING
from shared_utils import forEach as forEach
_mods: dict
_MOD_NAME_POSTFIX = '.pyc'

def init():
    ...
def fini():
    ...
def sendEvent(eventName, *args, **kwargs):
    ...
def _callModMethod(mod, methodName, *args, **kwargs):
    ...
def _isValidMOD(scriptName):
    ...
def _findValidMODs(path=None, package=None):
    ...
