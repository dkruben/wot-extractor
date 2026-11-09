# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/tooltips/ranked/ranked_prime_time.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/ranked/ranked_prime_time.py
from __future__ import absolute_import
from helpers import time_utils
from gui.shared.tooltips import ToolTipBaseData, TOOLTIP_TYPE
from helpers import dependency
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from predefined_hosts import g_preDefinedHosts
from skeletons.gui.game_control import IRankedBattlesController

class RankedServerPrimeTime(ToolTipBaseData):
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self, context):
        super(RankedServerPrimeTime, self).__init__(context, TOOLTIP_TYPE.CONTROL)

    def getDisplayableData(self, peripheryID):
        hostsList = g_preDefinedHosts.getSimpleHostsList(g_preDefinedHosts.hostsWithRoaming(), withShortName=True)
        serverName = ''
        for serverData in hostsList:
            _, serverName, _, _, pID = serverData
            if pID == peripheryID:
                break

        timeLeftStr = '-'
        isNow = False
        primeTime = self.__rankedController.getPrimeTimes().get(peripheryID)
        if primeTime:
            currentCycleEnd = self.__rankedController.getCurrentSeason().getCycleEndDate()
            isNow, timeLeft = primeTime.getAvailability(time_utils.getCurrentLocalServerTimestamp(), currentCycleEnd)
            timeLeftStr = backport.getTillTimeStringByRClass(timeLeft, R.strings.ranked_battles.status.timeLeft)
        formatedTime = text_styles.neutral(timeLeftStr)
        if isNow:
            descriptionID = R.strings.ranked_battles.primeTime.tooltip.server.available.untill()
        else:
            descriptionID = R.strings.ranked_battles.primeTime.tooltip.server.unavailable.inTime()
        sName = backport.text(R.strings.ranked_battles.primeTime.tooltip.server.onServer(), server=serverName)
        description = backport.text(descriptionID, time=formatedTime)
        return {'body': (('{}\n{}').format(sName, description))}
