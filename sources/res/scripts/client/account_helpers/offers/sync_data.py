# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/offers/sync_data.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/offers/sync_data.py
from __future__ import absolute_import
from account_helpers.AccountSyncData import BaseSyncDataCache
from shared_utils.account_helpers.diff_utils import synchronizeDicts

class OffersSyncData(BaseSyncDataCache):

    def _synchronize(self, diff):
        itemDiff = diff.get('offersData')
        if itemDiff is not None:
            synchronizeDicts(itemDiff, self._cache.setdefault('offersData', {}))
        return
