# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/shared/gun_state_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/shared/gun_state_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle.shared.timer_model import TimerModel

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
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(GunStateModel, self).__init__(properties=properties, commands=commands)

    @property
    def reloadTimer(self):
        return self._getViewModel(0)

    @staticmethod
    def getReloadTimerType():
        return TimerModel

    def getGunType(self):
        return GunType(self._getString(1))

    def setGunType(self, value):
        self._setString(1, value.value)

    def getReloadStatus(self):
        return ReloadStatus(self._getString(2))

    def setReloadStatus(self, value):
        self._setString(2, value.value)

    def getReloadMechanicType(self):
        return ReloadType(self._getString(3))

    def setReloadMechanicType(self, value):
        self._setString(3, value.value)

    def getCurrentShellQuantity(self):
        return self._getNumber(4)

    def setCurrentShellQuantity(self, value):
        self._setNumber(4, value)

    def getIsShotAvailable(self):
        return self._getBool(5)

    def setIsShotAvailable(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(GunStateModel, self)._initialize()
        self._addViewModelProperty('reloadTimer', TimerModel())
        self._addStringProperty('gunType', GunType.SIMPLE.value)
        self._addStringProperty('reloadStatus', ReloadStatus.READY.value)
        self._addStringProperty('reloadMechanicType', ReloadType.STANDARD.value)
        self._addNumberProperty('currentShellQuantity', -1)
        self._addBoolProperty('isShotAvailable', False)
