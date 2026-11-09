# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/currency_reserves/currency_reserves_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserve_model import CurrencyReserveModel as CurrencyReserveModel

class CurrencyReservesViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=3, commands=1):
        ...
    @property
    def creditReserve(self):
        ...
    @staticmethod
    def getCreditReserveType():
        ...
    @property
    def goldReserve(self):
        ...
    @staticmethod
    def getGoldReserveType():
        ...
    def getTimeToOpen(self):
        ...
    def setTimeToOpen(self, value):
        ...
    def _initialize(self):
        ...
