# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/Scaleform/daapi/view/tooltips/lobby_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/Scaleform/daapi/view/tooltips/lobby_builders.py
from __future__ import absolute_import
from advent_calendar.gui.Scaleform.daapi.view.tooltips.feature_tooltips import AdventCalendarNotRecruitedTooltipData, AdventCalendarCustomizationTooltipData
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.ADVENT_CALENDAR_TANKMAN_NOT_RECRUITED, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, AdventCalendarNotRecruitedTooltipData(contexts.NotRecruitedTankmanContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.ADVENT_CALENDAR_CUSTOMIZATION_ITEM, TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI, AdventCalendarCustomizationTooltipData(contexts.TechCustomizationContext())))
