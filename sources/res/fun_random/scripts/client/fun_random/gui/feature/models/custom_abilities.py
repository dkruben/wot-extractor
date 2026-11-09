# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/models/custom_abilities.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/models/custom_abilities.py
from __future__ import absolute_import
import typing
from items import vehicles
if typing.TYPE_CHECKING:
    from fun_random.gui.feature.configs.sub_modes.custom_abilities import FunSubModeCustomAbilityConfigModel, FunSubModeCustomAbilitySlotConfigModel, FunSubModeCustomAbilityLayoutConfigModel, FunSubModeCustomAbilitiesConfigModel
    from items.artefacts import Equipment

class FunCustomAbility(object):

    def __init__(self, intCD, imageName):
        self.intCD = intCD
        self.imageName = imageName

    @classmethod
    def fromEquipmentItem(cls, equipment):
        return cls(equipment.compactDescr, equipment.iconName)

    @classmethod
    def fromCustomEquipmentConfig(cls, abilityConfig):
        return cls.fromEquipmentItem(vehicles.getItemByCompactDescr(abilityConfig.intCD))


class FunCustomAbilitySlot(object):

    def __init__(self, slotConfig, customAbility):
        self.__slotConfig = slotConfig
        self.__customAbility = customAbility

    @classmethod
    def fromCustomLayoutConfig(cls, customAbilitiesConfig, layoutConfig):
        return cls(customAbilitiesConfig.slots[layoutConfig.slotIndex], FunCustomAbility.fromCustomEquipmentConfig(customAbilitiesConfig.abilities[layoutConfig.slotIndex]))

    @property
    def ability(self):
        return self.__customAbility

    @property
    def command(self):
        return self.__slotConfig.command

    @property
    def tooltipAlias(self):
        return self.__slotConfig.tooltipAlias
