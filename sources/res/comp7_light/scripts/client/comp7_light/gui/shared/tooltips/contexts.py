# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/shared/tooltips/contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/shared/tooltips/contexts.py
from __future__ import absolute_import
from gui.shared.tooltips import TOOLTIP_COMPONENT
from gui.shared.tooltips.contexts import ToolTipContext
from helpers import dependency
from items import vehicles
from skeletons.gui.game_control import IComp7LightController

class Comp7LightRoleSkillBattleContext(ToolTipContext):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    def __init__(self):
        super(Comp7LightRoleSkillBattleContext, self).__init__(TOOLTIP_COMPONENT.FULL_STATS)

    def buildItem(self, equipmentName):
        return vehicles.getEquipmentByName(equipmentName)

    def getStartLevel(self, roleName):
        return self.__comp7LightController.getEquipmentStartLevel(roleName)


class Comp7LightRoleSkillLobbyContext(ToolTipContext):

    def __init__(self):
        super(Comp7LightRoleSkillLobbyContext, self).__init__(TOOLTIP_COMPONENT.HANGAR)

    def buildItem(self, equipmentName):
        cache = vehicles.g_cache
        equipmentID = cache.equipmentIDs().get(equipmentName)
        if equipmentID is not None:
            return cache.equipments().get(equipmentID)
        else:
            return
