# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/easy_tank_equip_state.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/easy_tank_equip_state.py
from __future__ import absolute_import
import logging, typing
from CurrentVehicle import g_currentVehicle
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.hangar.random.sound_manager import EASY_TANK_EQUIP_SOUND_SPACE
from gui.lobby_state_machine.states import LobbyState, LobbyStateDescription
from helpers.events_handler import EventsHandler
from sound_gui_manager import ViewSoundExtension
_logger = logging.getLogger(__name__)

class EasyTankEquipStatePrototype(LobbyState, EventsHandler):
    __soundExtension = ViewSoundExtension(EASY_TANK_EQUIP_SOUND_SPACE)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.easyTankEquip()))

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)

    def _getEvents(self):
        return (
         (
          g_currentVehicle.onChangeStarted, self.__onVehicleChanged),)

    def _onEntered(self, event):
        super(EasyTankEquipStatePrototype, self)._onEntered(event)
        self._subscribe()
        relatedView = self.getMachine().getRelatedView(self)
        if relatedView is not None:
            easyTankEquip = relatedView.getChildByPosId(R.aliases.hangar.shared.EasyTankEquip())
            if easyTankEquip is not None:
                easyTankEquip.onEntered()
        self.__soundExtension.initSoundManager()
        self.__soundExtension.startSoundSpace()
        return

    def _onExited(self):
        self._unsubscribe()
        self.__soundExtension.destroySoundManager()
        relatedView = self.getMachine().getRelatedView(self)
        if relatedView is not None:
            easyTankEquip = relatedView.getChildByPosId(R.aliases.hangar.shared.EasyTankEquip())
            if easyTankEquip is not None:
                easyTankEquip.onExit()
        super(EasyTankEquipStatePrototype, self)._onExited()
        return

    def __onVehicleChanged(self):
        _logger.info('Vehicle changed while in EasyTankEquipState, navigating back')
        self.goBack()


def generateEasyTankEquipStates(hangarStateCls, easyTankEquipStateProtoCls=EasyTankEquipStatePrototype):

    @hangarStateCls.parentOf
    class easyTankEquipStateProtoCls(easyTankEquipStateProtoCls):
        STATE_ID = easyTankEquipStateProtoCls.STATE_ID or 'easyTankEquip'

    return (
     GeneratedEasyTankEquipState,)
