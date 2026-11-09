# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/common/preset_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel as PriceModel

class PresetDisableReason(Enum):
    NONE = 'none'
    DEMOUNT_NOT_POSSIBLE = 'demountNotPossible'
    NOT_ENOUGH_BUNKS = 'notEnoughBunks'

class PresetModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=5, commands=0):
        ...
    @property
    def price(self):
        ...
    @staticmethod
    def getPriceType():
        ...
    def getInstalled(self):
        ...
    def setInstalled(self, value):
        ...
    def getDisableReason(self):
        ...
    def setDisableReason(self, value):
        ...
    def getStoredItemsCount(self):
        ...
    def setStoredItemsCount(self, value):
        ...
    def getInstalledItemsCount(self):
        ...
    def setInstalledItemsCount(self, value):
        ...
    def _initialize(self):
        ...
