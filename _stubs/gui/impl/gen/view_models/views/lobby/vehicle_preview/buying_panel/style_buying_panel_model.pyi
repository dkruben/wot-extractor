# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/buying_panel/style_buying_panel_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel

class StyleBuyingStatus(IntEnum):
    AVAILABLE = 0
    NOTENOUGHMONEY = 1
    BPNOTPASSED = 2

class StyleBuyingPanelModel(ViewModel):
    __slots__: tuple
    onBuy: Any
    def __init__(self, properties=5, commands=1):
        ...
    def getLevel(self):
        ...
    def setLevel(self, value):
        ...
    def getPrice(self):
        ...
    def setPrice(self, value):
        ...
    def getCurrency(self):
        ...
    def setCurrency(self, value):
        ...
    def getUserCurrency(self):
        ...
    def setUserCurrency(self, value):
        ...
    def getStatus(self):
        ...
    def setStatus(self, value):
        ...
    def _initialize(self):
        ...
