# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/tooltips/comp7_light_lobby_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/tooltips/comp7_light_lobby_builders.py
from __future__ import absolute_import
from comp7_light.gui.Scaleform.daapi.view.lobby.tooltips.comp7_light_calendar_day_extended_tooltip import Comp7LightCalendarDayExtendedTooltip
from comp7_light.gui.Scaleform.daapi.view.lobby.tooltips.comp7_light_calendar_day_tooltip import Comp7LightCalendarDayTooltip
from comp7_light.gui.Scaleform.daapi.view.lobby.tooltips.comp7_light_selector_tooltip import Comp7LightSelectorTooltip
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_LIGHT_TOOLTIPS
from comp7_light.gui.shared.tooltips.comp7_light_tooltips import Comp7LightRoleSkillLobbyTooltipData
from comp7_light.gui.shared.tooltips.contexts import Comp7LightRoleSkillLobbyContext
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(COMP7_LIGHT_TOOLTIPS.COMP7_LIGHT_SELECTOR_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7LightSelectorTooltip(contexts.ToolTipContext(None))),
     DataBuilder(COMP7_LIGHT_TOOLTIPS.COMP7_LIGHT_CALENDAR_DAY_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7LightCalendarDayTooltip(contexts.ToolTipContext(None))),
     DataBuilder(COMP7_LIGHT_TOOLTIPS.COMP7_LIGHT_CALENDAR_DAY_EXTENDED_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7LightCalendarDayExtendedTooltip(contexts.ToolTipContext(None))),
     DataBuilder(COMP7_LIGHT_TOOLTIPS.COMP7_LIGHT_ROLE_SKILL_LOBBY_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, Comp7LightRoleSkillLobbyTooltipData(Comp7LightRoleSkillLobbyContext())))
