# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/skeletons/ls_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/skeletons/ls_controller.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from last_stand.gui.game_control.ls_controller import _LSConfig, _VehiclesConfig
    from Event import Event
    from gui.shared.utils.requesters import RequestCriteria

class ILSController(IGameController):
    onSettingsUpdate = None
    onEventDisabled = None

    @property
    def lootBoxesEvent(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def isBattlesEnabled(self):
        raise NotImplementedError

    def isPromoScreenEnabled(self):
        raise NotImplementedError

    def isIntroVideoEnabled(self):
        raise NotImplementedError

    def isInfoPageEnabled(self):
        raise NotImplementedError

    def isMetaInfoEnabled(self):
        raise NotImplementedError

    def isLootBoxEntryPointEnabled(self):
        raise NotImplementedError

    def isParallaxEnabled(self):
        raise NotImplementedError

    def isHangar3dPointVisible(self):
        raise NotImplementedError

    def isHangar3dPointRewardVisible(self):
        raise NotImplementedError

    def isAvailable(self):
        raise NotImplementedError

    def getModeSettings(self):
        raise NotImplementedError

    def getConfig(self):
        raise NotImplementedError

    def selectBattle(self, *args, **kwargs):
        raise NotImplementedError

    def openHangar(self):
        raise NotImplementedError

    def isEventPrb(self):
        raise NotImplementedError

    def selectRandomMode(self):
        raise NotImplementedError

    def getVehiclesConfig(self):
        raise NotImplementedError

    def getSuitableVehicles(self, criteria=None):
        raise NotImplementedError

    def getVehiclesCriteria(self):
        raise NotImplementedError
