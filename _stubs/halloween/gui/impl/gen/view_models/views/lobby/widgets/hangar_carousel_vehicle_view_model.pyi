# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/hangar_carousel_vehicle_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class VehicleTypes(Enum):
    NONE = 'none'
    LIGHTTANK = 'lightTank'
    MEDIUMTANK = 'mediumTank'
    HEAVYTANK = 'heavyTank'
    SPG = 'SPG'
    AT_SPG = 'AT-SPG'

class VehicleStates(Enum):
    DEFAULT = 'default'
    LOCKED = 'locked'
    INBATTLE = 'inBattle'
    INPLATOON = 'inPlatoon'
    INQUEUE = 'inQueue'

class CarouselTooltips(Enum):
    HALLOWEENCAROUSELVEHICLE = 'halloweenCarouselVehicle'
    HALLOWEENVEHICLEFEATURETOOLTIP = 'halloweenVehicleFeatureTooltip'
    DAILYQUEST = 'dailyQuest'

class HangarCarouselVehicleViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=7, commands=0):
        ...
    def getIntCD(self):
        ...
    def setIntCD(self, value):
        ...
    def getInvID(self):
        ...
    def setInvID(self, value):
        ...
    def getName(self):
        ...
    def setName(self, value):
        ...
    def getIconName(self):
        ...
    def setIconName(self, value):
        ...
    def getHasDaily(self):
        ...
    def setHasDaily(self, value):
        ...
    def getVehicleType(self):
        ...
    def setVehicleType(self, value):
        ...
    def getVehicleState(self):
        ...
    def setVehicleState(self, value):
        ...
    def _initialize(self):
        ...
