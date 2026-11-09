# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/dev_commands_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/dev_commands_control.py
from __future__ import absolute_import
import BigWorld, Keys
from constants import HAS_DEV_RESOURCES, IS_DEVELOPMENT
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand

class DevCommandsControl(InputHandlerCommand):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if BigWorld.isKeyDown(Keys.KEY_CAPSLOCK) and isDown and HAS_DEV_RESOURCES:
            avatar = BigWorld.player()
            if key == Keys.KEY_X:
                avatar.base.setDevelopmentFeature(0, 'reload_mechanics', 0, '')
                return False
        return False


def createDevCommandsControl():
    if IS_DEVELOPMENT:
        return DevCommandsControl()
    return InputHandlerCommand()
