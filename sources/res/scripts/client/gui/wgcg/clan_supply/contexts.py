# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/clan_supply/contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/clan_supply/contexts.py
import logging, typing
from gui.clans.data_wrapper import clan_supply
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
from shared_utils import makeTupleByDict
if typing.TYPE_CHECKING:
    from typing import Dict
_logger = logging.getLogger(__name__)

class ProgressionSettingsCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.CLAN_SUPPLY_GET_PROGRESSION_SETTINGS

    def getDataObj(self, incomeData):
        incomeData = incomeData or {}
        data = {}
        for pointID, pointSettings in incomeData.get('points', {}).items():
            data[pointID] = makeTupleByDict(clan_supply.PointSettings, pointSettings)

        incomeData.update({'points': data})
        return makeTupleByDict(clan_supply.ProgressionSettings, incomeData)

    def isAuthorizationRequired(self):
        return True


class ProgressionProgressCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.CLAN_SUPPLY_GET_PROGRESSION_PROGRESS

    def getDataObj(self, incomeData):
        incomeData = incomeData or {}
        data = {}
        for pointID, pointSettings in incomeData.get('points', {}).items():
            data[pointID] = makeTupleByDict(clan_supply.PointProgress, pointSettings)

        incomeData.update({'points': data})
        return makeTupleByDict(clan_supply.ProgressionProgress, incomeData)

    def isAuthorizationRequired(self):
        return True


class QuestsInfoCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.CLAN_SUPPLY_GET_QUESTS

    def getDataObj(self, incomeData):
        return clan_supply.makeQuestInfo(incomeData or {})

    def isAuthorizationRequired(self):
        return True


class PostQuestsInfoCtx(QuestsInfoCtx):

    def getRequestType(self):
        return WebRequestDataType.CLAN_SUPPLY_POST_QUESTS


class ClaimRewardsCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.CLAN_SUPPLY_CLAIM_QUESTS_REWARDS

    def isAuthorizationRequired(self):
        return True


class PurchaseProgressionStageCtx(CommonWebRequestCtx):

    def __init__(self, stageID, price):
        super(PurchaseProgressionStageCtx, self).__init__()
        self.__stageID = stageID
        self.__price = price

    def getRequestArgs(self):
        return (
         self.__stageID, self.__price)

    def getRequestType(self):
        return WebRequestDataType.CLAN_SUPPLY_PURCHASE_PROGRESSION_STAGE

    def isAuthorizationRequired(self):
        return True
