# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/battle_pass_service.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/battle_pass_service.py
from __future__ import absolute_import
import Event
from gui.impl.lobby.user_missions.hangar_widget.services import IBattlePassService
from gui.impl.lobby.user_missions.hangar_widget.services.service_events import ServiceEvents
from gui.prb_control.dispatcher import g_prbLoader
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController

class BattlePassService(IBattlePassService, ServiceEvents):
    __battlePassController = dependency.descriptor(IBattlePassController)

    def __init__(self):
        super(BattlePassService, self).__init__()
        self.onBattlePassChanged = Event.Event()
        self.startServiceEvents()

    def onPrbEntitySwitched(self):
        self._onBattlePassEvent()

    def isVisible(self):
        isVisible = not self.__battlePassController.isDisabled()
        isVisible &= self._isValidBattleTypeForBattlePass()
        return isVisible

    def startListening(self):
        self.startGlobalListening()
        self.__battlePassController.onBattlePassSettingsChange += self._onBattlePassEvent
        self.__battlePassController.onSeasonStateChanged += self._onBattlePassEvent

    def stopListening(self):
        self.stopGlobalListening()
        self.__battlePassController.onBattlePassSettingsChange -= self._onBattlePassEvent
        self.__battlePassController.onSeasonStateChanged -= self._onBattlePassEvent

    def finalize(self):
        self.stopListening()
        self.stopServiceEvents()
        self.onBattlePassChanged.clear()

    def _isValidBattleTypeForBattlePass(self):
        prbDispatcher = g_prbLoader.getDispatcher()
        if prbDispatcher is None:
            return False
        else:
            prbEntity = prbDispatcher.getEntity()
            if prbEntity is None:
                return False
            return self.__battlePassController.isValidBattleType(prbEntity)

    def _onBattlePassEvent(self, *_):
        self.onBattlePassChanged()
