# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/helpers/sync_data.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/helpers/sync_data.py
from __future__ import absolute_import
import typing
from account_helpers import AccountSyncData
from open_bundle_common.constants import OPEN_BUNDLE_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts
if typing.TYPE_CHECKING:
    from typing import Dict

class OpenBundleSyncData(object):

    def __init__(self):
        self.__cache = {}

    def clear(self):
        self.__cache.clear()

    def update(self, clientDiff):
        isFullSync = AccountSyncData.isFullSyncDiff(clientDiff)
        if isFullSync:
            self.__cache.clear()
        synchronizeDicts(clientDiff[OPEN_BUNDLE_PDATA_KEY], self.__cache)

    def getTrackedByNameSections(self, bundleID):
        return (self.__cache.get(bundleID) or {}).get('trackedByNameSections') or {}
