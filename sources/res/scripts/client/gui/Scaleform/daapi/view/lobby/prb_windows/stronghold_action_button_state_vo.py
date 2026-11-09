# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/stronghold_action_button_state_vo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/stronghold_action_button_state_vo.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.rally.action_button_state_vo import ActionButtonStateVO
from gui.prb_control.settings import UNIT_RESTRICTION
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS

class StrongholdActionButtonStateVO(ActionButtonStateVO):

    def __init__(self, unitEntity):
        if unitEntity.isStrongholdSettingsValid():
            rosterStats = unitEntity.getStats()
            rosterSettings = unitEntity.getRosterSettings()
            self.__isFirstBattle = unitEntity.isFirstBattle()
            self.__isSortie = unitEntity.isSortie()
            freeSlotsCount = rosterSettings.getMaxSlots() + 1 - rosterStats.occupiedSlotsCount - rosterStats.playersMatchingSlotsCount
            self.__hasFreeSlots = freeSlotsCount > 0
            self.__playersMatchingAvailable = unitEntity.isPlayersMatchingAvailable()
        else:
            self.__isFirstBattle = None
            self.__isSortie = None
            self.__hasFreeSlots = False
            self.__playersMatchingAvailable = False
        result = unitEntity.canPlayerDoAction()
        self.__unitIsValid, self.__restrictionType = result.isValid, result.restriction
        self.__isInPlayersMatching = unitEntity.inPlayersMatchingMode()
        super(StrongholdActionButtonStateVO, self).__init__(unitEntity)
        return

    def _getArenaStateStr(self):
        return (TOOLTIPS.STRONGHOLDS_TIMER_SQUADINBATTLE, {})

    def _getLabel(self):
        label = CYBERSPORT.WINDOW_UNIT_READY
        isFirstStrongholdBattle = self.__isFirstBattle and not self.__isSortie
        if self._playerInfo.isCommander() and not isFirstStrongholdBattle:
            label = CYBERSPORT.WINDOW_UNIT_FIGHT
        if self._playerInfo.isReady and self.__restrictionType != UNIT_RESTRICTION.IS_IN_IDLE:
            label = CYBERSPORT.WINDOW_UNIT_NOTREADY
        return label

    def _notInSlotMessage(self):
        if self._playerInfo.isLegionary() or not self.__hasFreeSlots:
            return (CYBERSPORT.WINDOW_UNIT_MESSAGE_CANDIDATE, {})
        return (
         CYBERSPORT.WINDOW_UNIT_MESSAGE_TAKESLOTINROSTER, {})

    def _getUnitReadyMessage(self):
        if self._playerInfo.isCommander():
            return ('', {})
        return super(StrongholdActionButtonStateVO, self)._getUnitReadyMessage()
