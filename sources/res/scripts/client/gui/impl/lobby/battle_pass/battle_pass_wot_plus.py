# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_wot_plus.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/battle_pass_wot_plus.py
from __future__ import absolute_import
import sys, typing
from helpers.dependency import replace_none_kwargs
from renewable_subscription_common.settings_constants import WotPlusTier
from renewable_subscription_common.settings_helpers import getCurrentModelTierSettings
from skeletons.gui.game_control import IWotPlusController, ISteamCompletionController, IBattlePassController
if typing.TYPE_CHECKING:
    pass
_MAX_INT = sys.maxsize

@replace_none_kwargs(wotPlusCtrl=IWotPlusController, steamCtrl=ISteamCompletionController, battlePassCtrl=IBattlePassController)
def getWotPlusBattlePassTier(wotPlusCtrl=None, steamCtrl=None, battlePassCtrl=None):
    settingsStorage = wotPlusCtrl.getSettingsStorage()
    if not settingsStorage.isBattlePassFeatureEnabled():
        return WotPlusTier.NONE
    if battlePassCtrl.isHoliday() or battlePassCtrl.isExtraChapter(battlePassCtrl.getCurrentChapterID()):
        return WotPlusTier.NONE
    if wotPlusCtrl.getSettingsStorage().isBattlePassFeatureAvailable():
        return wotPlusCtrl.getTier()
    return settingsStorage.getBestBattlePassBonusTier()


def isWotPlusBattlePassAvailableForAnyTier():
    return isValidWotPlusTier(getWotPlusBattlePassTier())


def isValidWotPlusTier(tierID):
    return tierID in WotPlusTier.ALL


def extractMinValueFromRange(fromIndex, toIndex, targetList):
    if fromIndex < 0:
        return 0
    minValue = _MAX_INT
    for i in range(fromIndex, min(toIndex, len(targetList))):
        if targetList[i] < minValue:
            minValue = targetList[i]

    if minValue == _MAX_INT:
        return 0
    return minValue


@replace_none_kwargs(wotPlus=IWotPlusController)
def getWotPlusPerBattlePoints(count, tierID, bonusType, vehTypeCompDescr=None, wotPlus=None):
    if not isValidWotPlusTier(tierID):
        return (0, 0)
    settingsStorage = wotPlus.getSettingsStorage()
    if not settingsStorage.isBattlePassFeatureEnabled():
        return (0, 0)
    wpWinList, wpLossList = getCurrentModelTierSettings(tierID).battlePassFeature.getVehiclePointListsForMode(bonusType, vehTypeCompDescr)
    extraWin = extractMinValueFromRange(0, count, wpWinList)
    extraLoss = extractMinValueFromRange(0, count, wpLossList)
    return (extraWin, extraLoss)


def getMergedWotPlusPointsList(tierID, bonusType, vehTypeCompDescr=None):
    if not isValidWotPlusTier(tierID):
        return tuple()
    wpWinList, wpLossList = getCurrentModelTierSettings(tierID).battlePassFeature.getVehiclePointListsForMode(bonusType, vehTypeCompDescr)
    wpWinList = list(wpWinList)
    wpLossList = list(wpLossList)
    if len(wpWinList) < len(wpLossList):
        wpWinList, wpLossList = wpLossList, wpWinList
    for i, wpW in enumerate(wpWinList):
        if wpW == 0:
            wpWinList[i] = wpLossList[i]

    return wpWinList
