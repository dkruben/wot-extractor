# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/armor_flashlight_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/armor_flashlight_control.py
from __future__ import absolute_import
import CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class ArmorFlashlightControl(InputHandlerCommand):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if isDown and CommandMapping.g_instance.isFired(CommandMapping.CMD_TOGGLE_ARMOR_FLASHLIGHT, key):
            armorFlashlightCtrl = self.__guiSessionProvider.shared.armorFlashlight
            return armorFlashlightCtrl.toggle()
        return False
