# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/util/fun_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/util/fun_helpers.py
from __future__ import absolute_import
import typing
from future.utils import viewitems
from fun_random.gui.feature.fun_constants import FEP_PROGRESSION_TRIGGER_QUEST_ID, FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID, FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID, FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID, FEP_PROGRESSION_COUNTER_ID, FEP_PROGRESSION_UNLIMITED_COUNTER_ID
from gui import GUI_NATIONS_ORDER_INDEX
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES
from helpers import dependency
from skeletons.gui.game_control import IFunRandomController
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle

def isFunProgressionTrigger(qID):
    return qID.startswith(FEP_PROGRESSION_TRIGGER_QUEST_ID) or qID.startswith(FEP_PROGRESSION_ALT_TRIGGER_QUEST_ID)


def isFunProgressionUnlimitedTrigger(qID):
    return qID.startswith(FEP_PROGRESSION_UNLIMITED_TRIGGER_QUEST_ID) or qID.startswith(FEP_PROGRESSION_UNLIMITED_ALT_TRIGGER_QUEST_ID)


def isFunProgressionCounter(qID):
    return qID.startswith(FEP_PROGRESSION_COUNTER_ID) or qID.startswith(FEP_PROGRESSION_UNLIMITED_COUNTER_ID)


@dependency.replace_none_kwargs(funRandomCtrl=IFunRandomController)
def canSelectFunRandomPrbEntity(funRandomCtrl=None):
    desiredSubMode = funRandomCtrl.subModesHolder.getDesiredSubMode()
    return funRandomCtrl.isEnabled() and desiredSubMode is not None and desiredSubMode.isAvailable()


def getProgressionInfoByExecutor(executorQuestID):
    progressionName, counterAmount = executorQuestID.split('_')[-2:]
    return (progressionName, int(counterAmount))


def getProgressionNameByTrigger(triggerQuestID):
    return triggerQuestID.split('_')[-2]


def getIdByTrigger(triggerQuestID):
    return triggerQuestID.split('_')[-1]


def getVehicleComparisonKey(vehicle):
    return (
     not vehicle.isInInventory,
     not vehicle.isEvent,
     not vehicle.isOnlyForBattleRoyaleBattles,
     not vehicle.isFavorite,
     GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
     VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
     vehicle.level,
     tuple(vehicle.buyPrices.itemPrice.price.iterallitems(byWeight=True)),
     vehicle.userName)


def notifyCaller(callback, result):
    if callback is not None:
        callback(result)
    return


def mergeIntervals(allPrimeTimes):
    primeTimes = {}
    for serverPrimeTimes in allPrimeTimes:
        for serverShortName in serverPrimeTimes:
            primeTimes[serverShortName] = primeTimes.get(serverShortName, []) + serverPrimeTimes[serverShortName]

    return {serverShortName: _normalizeIntervals(intervals) for serverShortName, intervals in viewitems(primeTimes)}


def _normalizeIntervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals)
    mergedIntervals = [intervals[0]]
    for interval in intervals[1:]:
        _, endFirst = mergedIntervals[-1]
        startSecond, endSecond = interval
        if startSecond <= endFirst < endSecond:
            mergedIntervals[-1][1] = endSecond
        elif startSecond > endFirst:
            mergedIntervals.append(interval)

    return mergedIntervals
