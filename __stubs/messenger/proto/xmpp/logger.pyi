# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/logger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from messenger.proto.xmpp.gloox_constants import LOG_LEVEL as LOG_LEVEL, LOG_SOURCE as LOG_SOURCE, GLOOX_EVENT as GLOOX_EVENT
from messenger.proto.xmpp.gloox_wrapper import ClientEventsHandler as ClientEventsHandler
from messenger.proto.xmpp.log_output import CLIENT_LOG_AREA as CLIENT_LOG_AREA, g_logOutput as g_logOutput

class _IEventLogger(object):
    def log(self, level, source, message):
        ...
    def clear(self):
        ...

class _GlooxLogger(_IEventLogger):
    def log(self, level, source, message):
        ...

class LogHandler(ClientEventsHandler):
    __slots__: tuple
    __loggers: Any
    def __init__(self):
        ...
    def logger(self, key):
        ...
    def getNames(self):
        ...
    def clear(self):
        ...
    def registerHandlers(self):
        ...
    def unregisterHandlers(self):
        ...
    def __handleLog(self, level, source, message):
        ...
    def __repr__(self):
        ...

class XMPP_EVENT_LOG(object):
    DISCONNECT = 1

def _getLogFunction(output, level):
    ...
def sendEventToServer(eventType, host, port, errorCode=0, errorDescr='', tries=1):
    ...
