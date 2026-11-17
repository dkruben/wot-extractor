# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/log_output.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
CLIENT_LOG_AREA_NAMES: dict
g_logOutput: Any

class CLIENT_LOG_AREA(object):
    GLOOX_SOURCE: Any
    GLOOX_XML: Any
    PY_WRAPPER: Any
    CONNECTION: Any
    LOGIN: Any
    TOKEN: Any
    ROSTER: Any
    GROUP: Any
    SETTINGS: Any
    GENERIC: Any
    SYNC: Any
    BLOCK_LIST: Any
    RESOURCE: Any
    SUBSCRIPTION: Any
    MESSAGE: Any
    OBSOLETE: Any

class ILogOutput(object):
    def debug(self, area, message, *args, **kwargs):
        ...
    def warning(self, area, message, *args, **kwargs):
        ...
    def error(self, area, message, *args, **kwargs):
        ...
    def clear(self):
        ...

class ConsoleLogOutput(ILogOutput):
    def debug(self, area, message, *args):
        ...
    def warning(self, area, message, *args):
        ...
    def error(self, area, message, *args):
        ...
    def __makeHeader(self, area, message):
        ...

class _LogOutputDecorator(ILogOutput):
    __slots__: tuple
    __outputs: Any
    def __init__(self):
        ...
    def addOutput(self, name, output):
        ...
    def removeOutput(self, name):
        ...
    def getOutput(self, name):
        ...
    def debug(self, area, message, *args):
        ...
    def warning(self, area, message, *args):
        ...
    def error(self, area, message, *args):
        ...
    def clear(self):
        ...
