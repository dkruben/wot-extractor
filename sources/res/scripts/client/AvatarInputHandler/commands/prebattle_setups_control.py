# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/prebattle_setups_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/prebattle_setups_control.py
from __future__ import absolute_import
import CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from gui.battle_control import event_dispatcher
_SETUP_CMDS = (
 CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_1,
 CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_2)

class PrebattleSetupsControl(InputHandlerCommand):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if CommandMapping.g_instance.isFiredList(_SETUP_CMDS, key) and isDown:
            event_dispatcher.changeAmmunitionSetup(key)
            return True
        return False
