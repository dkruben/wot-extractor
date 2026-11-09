# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/tooltips/lobby_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/tooltips/lobby_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
from fun_random.gui.fun_gui_constants import FunRandomTooltipConstants
from fun_random.gui.Scaleform.daapi.view.lobby.feature.tooltips.calendar_day_tooltip import FunRandomCalendarDayTooltip, FunRandomModeSelectorCalendarTooltip
from fun_random.gui.Scaleform.daapi.view.lobby.feature.tooltips.rewards_tooltip import FunRandomRewardsTooltip
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(FunRandomTooltipConstants.FUN_RANDOM_CALENDAR_DAY, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, FunRandomCalendarDayTooltip(contexts.ToolTipContext(None))),
     DataBuilder(FunRandomTooltipConstants.FUN_RANDOM_MODE_SELECTOR_CALENDAR_DAY, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, FunRandomModeSelectorCalendarTooltip(contexts.ToolTipContext(None))),
     DataBuilder(FunRandomTooltipConstants.FUN_RANDOM_REWARDS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, FunRandomRewardsTooltip(contexts.ToolTipContext(None))))
