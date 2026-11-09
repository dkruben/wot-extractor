# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/shared/tooltips/comp7_light_tooltips.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/shared/tooltips/comp7_light_tooltips.py
from __future__ import absolute_import
from comp7_core.gui.shared.tooltips.comp7_core_tooltips import RoleSkillLobbyTooltipData, RoleSkillBattleTooltipData
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightRoleSkillLobbyTooltipData(RoleSkillLobbyTooltipData):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController


class Comp7LightRoleSkillBattleTooltipData(RoleSkillBattleTooltipData):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController
