# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/research/buy_module_dialog_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel as FullScreenDialogWindowModel

class MountDisabledReason(Enum):
    INVALID = 'invalid'
    NONE = 'none'
    NEEDGUN = 'need gun'
    NOTFORVEHICLETYPE = 'not for this vehicle type'
    NOTFORCURRENTVEHICLE = 'not for current vehicle'
    NEEDTURRET = 'need turret'

class ModuleType(Enum):
    FUELTANK = 'vehicleFuelTank'
    CHASSIS = 'vehicleChassis'
    WHEELEDCHASSIS = 'vehicleWheeledChassis'
    ENGINE = 'vehicleEngine'
    RADIO = 'vehicleRadio'
    TURRET = 'vehicleTurret'
    GUN = 'vehicleGun'

class BuyModuleDialogViewModel(FullScreenDialogWindowModel):
    __slots__: tuple
    def __init__(self, properties=17, commands=3):
        ...
    def getModuleType(self):
        ...
    def setModuleType(self, value):
        ...
    def getModulePrice(self):
        ...
    def setModulePrice(self, value):
        ...
    def getPreviousModuleName(self):
        ...
    def setPreviousModuleName(self, value):
        ...
    def getPreviousModulePrice(self):
        ...
    def setPreviousModulePrice(self, value):
        ...
    def getAutoSellEnabled(self):
        ...
    def setAutoSellEnabled(self, value):
        ...
    def getMountDisabledReason(self):
        ...
    def setMountDisabledReason(self, value):
        ...
    def _initialize(self):
        ...
