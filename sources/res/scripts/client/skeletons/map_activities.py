# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/map_activities.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/map_activities.py


class IMapActivities(object):
    __slots__ = ()

    def start(self, name, targetTime):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def generateOfflineActivities(self, spacePath, usePossibility=True):
        raise NotImplementedError

    def setPauseVisuals(self, isPause):
        raise NotImplementedError
