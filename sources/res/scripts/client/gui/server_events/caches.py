# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/server_events/caches.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/caches.py


class _NavigationInfo(object):

    def __init__(self):
        self.tabID = None
        self._missionsTab = None
        self._marathonPrefix = None
        self._vehicleSelectorFilters = {}
        return

    def getMissionsTab(self):
        return self._missionsTab

    def getMarathonPrefix(self):
        return self._marathonPrefix

    def setMissionsTab(self, tabID):
        self._missionsTab = tabID

    def setMarathonPrefix(self, marathonPrefix):
        self._marathonPrefix = marathonPrefix

    def getVehicleSelectorFilters(self):
        return self._vehicleSelectorFilters

    def setVehicleSelectorFilters(self, filters):
        self._vehicleSelectorFilters = filters


_g_navInfo = None

def getNavInfo():
    global _g_navInfo
    if _g_navInfo is None:
        _g_navInfo = _NavigationInfo()
    return _g_navInfo


def clearNavInfo():
    global _g_navInfo
    _g_navInfo = None
    return
