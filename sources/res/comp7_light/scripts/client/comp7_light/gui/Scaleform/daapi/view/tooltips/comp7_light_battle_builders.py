# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/tooltips/comp7_light_battle_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/tooltips/comp7_light_battle_builders.py
from __future__ import absolute_import
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_BATTLE_CONSTANTS import TOOLTIPS_BATTLE_CONSTANTS as COMP7_LIGHT_BATTLE_TOOLTIPS
from comp7_light.gui.shared.tooltips.comp7_light_tooltips import Comp7LightRoleSkillBattleTooltipData
from comp7_light.gui.shared.tooltips.contexts import Comp7LightRoleSkillBattleContext
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts, vehicle_roles
from gui.shared.tooltips.builders import DataBuilder, TooltipWindowBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(COMP7_LIGHT_BATTLE_TOOLTIPS.COMP7_LIGHT_ROLE_SKILL_BATTLE_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7LightRoleSkillBattleTooltipData(Comp7LightRoleSkillBattleContext())),
     TooltipWindowBuilder(TOOLTIPS_CONSTANTS.VEHICLE_ROLES, None, vehicle_roles.VehicleRolesTooltipContentWindowData(contexts.ToolTipContext(None))))
