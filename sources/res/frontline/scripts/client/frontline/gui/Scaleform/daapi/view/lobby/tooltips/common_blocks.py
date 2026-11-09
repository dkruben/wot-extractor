# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/tooltips/common_blocks.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/tooltips/common_blocks.py
from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import getTimeToEndStr, getTimeToStartStr
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.formatters.ranges import toRomanRangeString
from gui.shared.tooltips import formatters
from helpers import time_utils, dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController)
def packEpicBattleInfoBlock(epicController=None):
    descLvl = text_styles.stats(backport.text(R.strings.epic_battle.selectorTooltip.epicBattle.bodyVehicleLevel(), level=toRomanRangeString(epicController.getValidVehicleLevels())))
    season = epicController.getCurrentSeason()
    currentTime = time_utils.getCurrentLocalServerTimestamp()
    descr = R.strings.epic_battle.selectorTooltip.epicBattle.ended.body()
    if currentTime < season.getLastCycleInfo().endDate:
        descr = R.strings.epic_battle.selectorTooltip.epicBattle.body()
    return formatters.packTitleDescBlock(title=text_styles.middleTitle(backport.text(R.strings.epic_battle.tooltips.common.title())), desc=text_styles.main(backport.text(descr, bodyVehicleLevel=descLvl)), padding=formatters.packPadding(top=20, left=20, right=20), descPadding=formatters.packPadding(right=30))


@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController)
def packEpicBattleSeasonBlock(epicController=None):
    if not epicController.isEnabled():
        return
    else:
        season = epicController.getCurrentSeason() or epicController.getNextSeason()
        currentTime = time_utils.getCurrentLocalServerTimestamp()
        if epicController.isCurrentCycleActive():
            cycle = season.getCycleInfo()
            getDate = lambda c: c.endDate
            getTimeToStr = getTimeToEndStr
        else:
            cycle = season.getNextByTimeCycle(currentTime) if season else None
            if cycle and cycle.announceOnly:
                return
            getDate = lambda c: c.startDate
            getTimeToStr = getTimeToStartStr
        if cycle is not None:
            description = getTimeToStr(getDate(cycle) - currentTime)
        else:
            description = backport.text(R.strings.epic_battle.tooltips.widget.finished())
        return formatters.packBuildUpBlockData([
         formatters.packImageTextBlockData(desc=text_styles.main(description), padding=formatters.packPadding(left=20, right=20))])
