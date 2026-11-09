# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_calendar_steps_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/ranked/ranked_calendar_steps_tooltip.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.tooltips import TOOLTIP_TYPE
from gui.shared.tooltips import formatters
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency
from helpers import time_utils
from season_common import CycleStatus
from skeletons.gui.game_control import IRankedBattlesController
_TOOLTIP_MIN_WIDTH = 200

class RankedCalendarStepsTooltip(BlocksTooltipData):
    rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self, ctx):
        super(RankedCalendarStepsTooltip, self).__init__(ctx, TOOLTIP_TYPE.RANKED_CALENDAR_DAY)
        self._setContentMargin(top=18, left=20, bottom=18, right=20)
        self._setMargins(afterBlock=13)
        self._setWidth(_TOOLTIP_MIN_WIDTH)

    def _packBlocks(self):
        items = super(RankedCalendarStepsTooltip, self)._packBlocks()
        blocks = [self.__packHeaderBlock()]
        key = R.strings.ranked_battles.rankedBattleView.statusBlock.calendarPopover.cycleItem()
        currentSeason = self.rankedController.getCurrentSeason()
        cycles = currentSeason.getAllCycles()
        seasonName = currentSeason.getNumber()
        for cycle in sorted(cycles.values()):
            currentCycle = False
            if cycle.status == CycleStatus.CURRENT:
                formatter = text_styles.main
                currentCycle = True
            else:
                formatter = text_styles.standard
            startDate = time_utils.getTimeStructInLocal(cycle.startDate)
            endDate = time_utils.getTimeStructInLocal(cycle.endDate)
            item = formatter(backport.text(key, cycleNumber=seasonName, day0=('{:02d}').format(startDate.tm_mday), month0=('{:02d}').format(startDate.tm_mon), day1=('{:02d}').format(endDate.tm_mday), month1=('{:02d}').format(endDate.tm_mon)))
            if currentCycle:
                blocks.append(formatters.packImageTextBlockData(title=item, img=backport.image(R.images.gui.maps.icons.library.inProgressIcon()), imgPadding=formatters.packPadding(top=5), txtPadding=formatters.packPadding(left=5)))
            else:
                blocks.append(formatters.packTextBlockData(text=item, padding=formatters.packPadding(left=20)))

        items.append(formatters.packBuildUpBlockData(blocks, 13))
        return items

    def __packHeaderBlock(self):
        return formatters.packImageTextBlockData(title=text_styles.middleTitle(backport.text(R.strings.ranked_battles.calendarStepsTooltip.title())), img=backport.image(R.images.gui.maps.icons.buttons.calendar()), imgPadding=formatters.packPadding(top=5), txtPadding=formatters.packPadding(left=10))
