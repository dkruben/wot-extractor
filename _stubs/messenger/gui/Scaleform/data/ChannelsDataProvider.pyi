# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/data/ChannelsDataProvider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import itervalues as itervalues
import BigWorld as BigWorld
import Event as Event
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control.events_dispatcher import TOOLTIP_PRB_DATA as TOOLTIP_PRB_DATA
DEFAULT_FIELDS: dict

class ChannelsDataProvider(object):
    __data: Any
    __list: Any
    onDataUpdated: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def addItem(self, clientID, data):
        ...
    def removeItem(self, clientID):
        ...
    def setItemField(self, clientID, key, value):
        ...
    def clearItemField(self, clientID, key):
        ...
    def setItemFields(self, clientID, fields):
        ...
    @property
    def collection(self):
        ...
    def buildList(self):
        ...
    def refresh(self):
        ...
