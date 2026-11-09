# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/auto_shoot_gun_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/mechanic_controls/auto_shoot_gun_control.py
from __future__ import absolute_import
import Keys
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from gui.battle_control.controllers.auto_shoot_guns.auto_shoot_helpers import AUTO_SHOOT_DEV_KEYS, AutoShootDevCommand
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class DevAutoShootGunControl(InputHandlerCommand):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    _KEY_TO_COMMAND_MAP = {(Keys.KEY_RIGHTARROW): (AutoShootDevCommand.RATE_UP), 
       (Keys.KEY_LEFTARROW): (AutoShootDevCommand.RATE_DOWN), 
       (Keys.KEY_UPARROW): (AutoShootDevCommand.RATE_SPEED_UP), 
       (Keys.KEY_DOWNARROW): (AutoShootDevCommand.RATE_SPEED_DOWN), 
       (Keys.KEY_RSHIFT): (AutoShootDevCommand.CLAMP_BURST), 
       (Keys.KEY_RCONTROL): (AutoShootDevCommand.RESET)}

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if not self.__handleDevKeyEvent(isDown, key):
            return super(DevAutoShootGunControl, self).handleKeyEvent(isDown, key, mods, event=event)
        return True

    def __handleDevKeyEvent(self, isDown, key):
        if not (key in self._KEY_TO_COMMAND_MAP and isDown):
            return False
        else:
            autoShootCtrl = self.__sessionProvider.shared.autoShootCtrl
            if autoShootCtrl is None:
                return False
            autoShootCtrl.processAutoShootDevCmd(self._KEY_TO_COMMAND_MAP[key])
            return True


def createAutoShootGunControl(*_, **__):
    if AUTO_SHOOT_DEV_KEYS:
        return DevAutoShootGunControl()
    return InputHandlerCommand()
