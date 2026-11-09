# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/account_dashboard/map_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class SlotStateEnum(Enum):
    EMPTY = 'empty'
    SELECTED = 'selected'
    DISABLED = 'disabled'

class SlotTypeEnum(Enum):
    NONE = 'none'
    PREMIUM = 'premium'
    WOTPLUS = 'wotplus'

class MapModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getCooldownEndTimeInSecs(self):
        ...
    def setCooldownEndTimeInSecs(self, value):
        ...
    def getMapId(self):
        ...
    def setMapId(self, value):
        ...
    def getSlotState(self):
        ...
    def setSlotState(self, value):
        ...
    def getSlotType(self):
        ...
    def setSlotType(self, value):
        ...
    def _initialize(self):
        ...
