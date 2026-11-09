# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/Scaleform/daapi/view/tooltips/feature_tooltips.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/Scaleform/daapi/view/tooltips/feature_tooltips.py
from __future__ import absolute_import
from advent_calendar.gui.Scaleform.daapi.view.tooltips.common_blocks import AdventCalendarProgressionRewardTooltipData
from gui.Scaleform.daapi.view.lobby.customization.tooltips import ElementAwardTooltip
from gui.shared.tooltips.tankman import NotRecruitedTooltipData

class AdventCalendarNotRecruitedTooltipData(NotRecruitedTooltipData):

    def _packBlocks(self, *args, **kwargs):
        invID, questID = args
        items = super(AdventCalendarNotRecruitedTooltipData, self)._packBlocks(invID)
        items.append(AdventCalendarProgressionRewardTooltipData.packProgressionBlock(questID))
        return items


class AdventCalendarCustomizationTooltipData(ElementAwardTooltip):

    def _packBlocks(self, questID, *args, **kwargs):
        items = super(AdventCalendarCustomizationTooltipData, self)._packBlocks(*args)
        items.append(AdventCalendarProgressionRewardTooltipData.packProgressionBlock(questID))
        return items
