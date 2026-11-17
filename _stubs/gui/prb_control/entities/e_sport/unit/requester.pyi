# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/e_sport/unit/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
import BigWorld as BigWorld
from UnitBase import UNIT_ERROR as UNIT_ERROR
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from helpers import time_utils as time_utils
_logger: Any

class UnitAutoSearchHandler(object):
    __entity: Any
    __vTypeDescrs: Any
    __isInSearch: Any
    __hasResult: Any
    __startSearchTime: Any
    __lastErrorCode: Any
    def __init__(self, entity):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def initEvents(self, listener):
        ...
    def isInSearch(self):
        ...
    def getTimeLeftInSearch(self):
        ...
    def getAcceptDelta(self, acceptDeadlineUTC):
        ...
    def start(self, vTypeDescrs=None):
        ...
    def stop(self):
        ...
    def accept(self):
        ...
    def decline(self):
        ...
    def unitBrowser_onErrorReceived(self, errorCode, errorStr):
        ...

def _logDeprecationError():
    ...
