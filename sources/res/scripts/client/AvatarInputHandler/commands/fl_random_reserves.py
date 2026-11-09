# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/fl_random_reserves.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/fl_random_reserves.py
from __future__ import absolute_import
import CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from ReservesEvents import randomReservesEvents
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class FLRandomReserves(InputHandlerCommand):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    __FIRST_RESERVE_INDEX = 0
    __SECOND_RESERVE_INDEX = 1

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if CommandMapping.g_instance.isFiredList([
         CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_LEFT,
         CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_ALTERNATIVE_LEFT], key):
            randomReservesEvents.onSelectedReserve(self.__FIRST_RESERVE_INDEX)
            return True
        if CommandMapping.g_instance.isFiredList([
         CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_RIGHT,
         CommandMapping.CMD_CM_VEHICLE_UPGRADE_PANEL_ALTERNATIVE_RIGHT], key):
            randomReservesEvents.onSelectedReserve(self.__SECOND_RESERVE_INDEX)
            return True
        return False
