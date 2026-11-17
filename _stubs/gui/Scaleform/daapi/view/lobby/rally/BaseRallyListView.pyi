# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rally/BaseRallyListView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from abc import abstractmethod as abstractmethod
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.meta.BaseRallyListViewMeta import BaseRallyListViewMeta as BaseRallyListViewMeta
from messenger.proto.events import g_messengerEvents as g_messengerEvents

class BaseRallyListView(BaseRallyListViewMeta):
    _searchDP: Any
    def __init__(self):
        ...
    @abstractmethod
    def getPyDataProvider(self):
        ...
    def setData(self, initialData):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def getRallyDetails(self, index):
        ...
    def _updateVehiclesLabel(self, minVal, maxVal):
        ...
    def _onUserActionReceived(self, _, user, shadowMode):
        ...
