# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/premacc/maps_blacklist_slot_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class MapStateEnum(Enum):
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE = 'active'
    MAPS_BLACKLIST_SLOT_STATE_CHANGE = 'change'
    MAPS_BLACKLIST_SLOT_STATE_DISABLED = 'disabled'
    MAPS_BLACKLIST_SLOT_STATE_COOLDOWN = 'cooldown'
    MAPS_BLACKLIST_SLOT_STATE_SELECTED = 'selected'
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER = 'active_no_hover'

class SlotTypeEnum(Enum):
    NONE = 'none'
    PREMIUM = 'premium'
    WOTPLUS = 'wotplus'

class MapsBlacklistSlotModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getMapId(self):
        ...
    def setMapId(self, value):
        ...
    def getSeasonId(self):
        ...
    def setSeasonId(self, value):
        ...
    def getCooldownTime(self):
        ...
    def setCooldownTime(self, value):
        ...
    def getFiltered(self):
        ...
    def setFiltered(self, value):
        ...
    def getSlotType(self):
        ...
    def setSlotType(self, value):
        ...
    def _initialize(self):
        ...
