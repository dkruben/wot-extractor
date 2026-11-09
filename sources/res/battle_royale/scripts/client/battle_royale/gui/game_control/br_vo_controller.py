# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/br_vo_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/game_control/br_vo_controller.py
from __future__ import absolute_import
import BigWorld, WWISE, nations
from constants import CURRENT_REALM, IS_CHINA
from gui.battle_control import avatar_getter
from items import vehicles
from helpers import isPlayerAvatar
_RU_REALMS = ('DEV', 'QA', 'RU')
_SWITCH_RU = 'SWITCH_ext_BR_vo_language'
_SWITCH_RU_ON = 'SWITCH_ext_BR_vo_language_RU'
_SWITCH_RU_OFF = 'SWITCH_ext_BR_vo_language_nonRU'
_SWITCH_CN = 'SWITCH_ext_BR_vo_language_CN'
_SWITCH_CHAR = 'SWITCH_ext_BR_vo_char'
_SWITCH_CHAR_FOR_NATIONS = {'ussr': 'SWITCH_ext_BR_vo_char_RU', 
   'usa': 'SWITCH_ext_BR_vo_char_US', 
   'germany': 'SWITCH_ext_BR_vo_char_GE', 
   'france': 'SWITCH_ext_BR_vo_char_FR', 
   'uk': 'SWITCH_ext_BR_vo_char_UK', 
   'sweden': 'SWITCH_ext_BR_vo_char_SE', 
   'china': 'SWITCH_ext_BR_vo_char_CN', 
   'poland': 'SWITCH_ext_BR_vo_char_PL'}

class BRVoiceOverController(object):

    def __init__(self):
        super(BRVoiceOverController, self).__init__()
        self.__isActive = False

    def init(self):
        WWISE.WW_setRealm(CURRENT_REALM)

    def fini(self):
        pass

    def activate(self):
        self.__isActive = True
        if isPlayerAvatar():
            self.__updateBattleSwitches(BigWorld.player().getVehicleAttached())

    def deactivate(self):
        self.__isActive = False

    def onAvatarBecomePlayer(self):
        avatar = BigWorld.player()
        playerVehicle = avatar.getVehicleAttached()
        if playerVehicle is not None:
            self.__updateBattleSwitches(playerVehicle)
        else:
            avatar.onVehicleEnterWorld += self.__onVehicleEnterWorld
        return

    def __onVehicleEnterWorld(self, vehicle):
        if vehicle.id == avatar_getter.getVehicleIDAttached():
            BigWorld.player().onVehicleEnterWorld -= self.__onVehicleEnterWorld
            self.__updateBattleSwitches(vehicle)

    def __updateBattleSwitches(self, vehicle):
        if self.__isActive:
            if vehicle is not None:
                compactDescr = vehicle.typeDescriptor.type.compactDescr
                WWISE.WW_setSwitch(_SWITCH_CHAR, self.__compactDescrToSwitchValue(compactDescr))
            WWISE.WW_setSwitch(_SWITCH_RU, self.__switchRuValue)
        return

    def __compactDescrToSwitchValue(self, descr):
        _, nationIdx, _ = vehicles.parseIntCompactDescr(descr)
        nationName = nations.NAMES[nationIdx]
        return _SWITCH_CHAR_FOR_NATIONS[nationName]

    @property
    def __isRuRealm(self):
        return CURRENT_REALM in _RU_REALMS

    @property
    def __switchRuValue(self):
        if IS_CHINA:
            return _SWITCH_CN
        if self.__isRuRealm:
            return _SWITCH_RU_ON
        return _SWITCH_RU_OFF
