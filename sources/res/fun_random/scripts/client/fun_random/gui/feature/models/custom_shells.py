# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/models/custom_shells.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/models/custom_shells.py
from __future__ import absolute_import
import typing
from items import vehicles
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.vehicle_modules import Shell
    from fun_random.gui.feature.configs.sub_modes.custom_shells import FunSubModeCustomShellConfigModel, FunSubModeCustomShellSlotConfigModel, FunSubModeCustomShellLayoutConfigModel, FunSubModeCustomShellsConfigModel

class FunCustomShell(object):

    def __init__(self, intCD, count, imageName):
        self.intCD = intCD
        self.count = count
        self.imageName = imageName

    @classmethod
    def fromShellItem(cls, shell):
        return cls(shell.intCD, shell.count, shell.descriptor.iconName)

    @classmethod
    def fromCustomShellConfig(cls, shellConfig, count):
        return cls(shellConfig.intCD, count, vehicles.getItemByCompactDescr(shellConfig.intCD).iconName)


class FunCustomShellSlot(object):

    def __init__(self, slotConfig, customShell, originalIndex):
        self.__slotConfig = slotConfig
        self.__customShell = customShell
        self.__originalIndex = originalIndex

    @classmethod
    def fromShellItem(cls, customShellsConfig, layoutConfig, shell):
        return cls(customShellsConfig.slots[layoutConfig.slotIndex], FunCustomShell.fromShellItem(shell), layoutConfig.shellIndex)

    @classmethod
    def fromCustomLayoutConfig(cls, customShellsConfig, layoutConfig):
        return cls(customShellsConfig.slots[layoutConfig.slotIndex], FunCustomShell.fromCustomShellConfig(customShellsConfig.shells[layoutConfig.slotIndex], layoutConfig.shellCount), layoutConfig.shellIndex)

    @property
    def originalIndex(self):
        return self.__originalIndex

    @property
    def command(self):
        return self.__slotConfig.command

    @property
    def shell(self):
        return self.__customShell

    @property
    def imageNameOverride(self):
        return self.__slotConfig.imageOverride

    @property
    def tooltipOverride(self):
        return self.__slotConfig.tooltipOverride
