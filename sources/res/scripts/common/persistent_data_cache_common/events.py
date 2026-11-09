# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/persistent_data_cache_common/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/persistent_data_cache_common/events.py
from __future__ import absolute_import
from Event import EventManager, SafeEvent

class DefaultPDCEventsDispatcher(object):
    __slots__ = ('onDataDeserialized', 'onCachedDataLoaded', 'onFailedToLoadCachedData',
                 'onCachedDataSaved', 'onFailedToSaveCachedData', '_manager', 'onCacheDataSavingStarted')

    def __init__(self):
        super(DefaultPDCEventsDispatcher, self).__init__()
        self._manager = EventManager()
        self.onDataDeserialized = SafeEvent(self._manager)
        self.onCachedDataLoaded = SafeEvent(self._manager)
        self.onFailedToLoadCachedData = SafeEvent(self._manager)
        self.onCacheDataSavingStarted = SafeEvent(self._manager)
        self.onCachedDataSaved = SafeEvent(self._manager)
        self.onFailedToSaveCachedData = SafeEvent(self._manager)

    def fini(self):
        if self._manager:
            self._manager.clear()
            self._manager = None
        return
