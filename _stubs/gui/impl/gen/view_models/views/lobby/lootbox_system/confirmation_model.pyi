# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/confirmation_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel

class ConfirmationModel(ViewModel):
    __slots__: tuple
    confirm: Any
    cancel: Any
    def __init__(self, properties=2, commands=2):
        ...
    @property
    def price(self):
        ...
    @staticmethod
    def getPriceType():
        ...
    def getEventName(self):
        ...
    def setEventName(self, value):
        ...
    def _initialize(self):
        ...
