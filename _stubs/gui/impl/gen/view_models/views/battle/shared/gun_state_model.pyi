# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/shared/gun_state_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.battle.shared.timer_model import TimerModel as TimerModel

class GunType(Enum):
    SIMPLE = 'simple'
    AUTORELOAD = 'autoReload'
    DUALGUN = 'dualGun'
    CONTROLLABLE = 'controllable'

class ReloadStatus(Enum):
    READY = 'ready'
    RELOADING = 'reloading'
    EMPTY = 'empty'

class ReloadType(Enum):
    STANDARD = 'standard'
    CASSETTECLIP = 'cassetteClip'
    AUTOLOADERCLIP = 'autoLoaderClip'
    EXTRASHOTCLIP = 'extraShotClip'
    CONTROLLABLERELOAD = 'controllableReload'
    UNLIMITEDCLIP = 'unlimitedClip'
    SHELLCALIBRATIONCLIP = 'shellCalibrationClip'

class GunStateModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    @property
    def reloadTimer(self):
        ...
    @staticmethod
    def getReloadTimerType():
        ...
    def getGunType(self):
        ...
    def setGunType(self, value):
        ...
    def getReloadStatus(self):
        ...
    def setReloadStatus(self, value):
        ...
    def getReloadMechanicType(self):
        ...
    def setReloadMechanicType(self, value):
        ...
    def getCurrentShellQuantity(self):
        ...
    def setCurrentShellQuantity(self, value):
        ...
    def getIsShotAvailable(self):
        ...
    def setIsShotAvailable(self, value):
        ...
    def _initialize(self):
        ...
