# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/confirmation_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel

class ConfirmationModel(ViewModel):
    __slots__: tuple
    confirm: Any
    cancel: Any
    def __init__(self, properties=4, commands=2):
        ...
    @property
    def price(self):
        ...
    @staticmethod
    def getPriceType():
        ...
    def getBundleType(self):
        ...
    def setBundleType(self, value):
        ...
    def getBalance(self):
        ...
    def setBalance(self, value):
        ...
    @staticmethod
    def getBalanceType():
        ...
    def getIsWalletAvailable(self):
        ...
    def setIsWalletAvailable(self, value):
        ...
    def _initialize(self):
        ...
