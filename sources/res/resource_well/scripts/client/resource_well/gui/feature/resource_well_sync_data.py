# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/feature/resource_well_sync_data.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/feature/resource_well_sync_data.py
from __future__ import absolute_import
from typing import Dict
from account_helpers import AccountSyncData
from resource_well_common.feature_constants import RESOURCE_WELL_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts

class ResourceWellSyncData(object):

    def __init__(self):
        self.__cache = {}

    def clear(self):
        self.__cache.clear()

    def getSeason(self):
        return self.__cache.get('season', 0)

    def getCurrentPoints(self):
        return self.__cache.get('points', 0)

    def getBalance(self):
        return self.__cache.get('balance', {})

    def getReward(self):
        return self.__cache.get('reward', set())

    def getCurrentRewardID(self):
        return self.__cache.get('currentRewardId', '')

    def getInitialNumberAmounts(self):
        return self.__cache.get('initialAmounts', {})

    def update(self, clientDiff):
        isFullSync = AccountSyncData.isFullSyncDiff(clientDiff)
        if isFullSync:
            self.__cache.clear()
        synchronizeDicts(clientDiff[RESOURCE_WELL_PDATA_KEY], self.__cache)
