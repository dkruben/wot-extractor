# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/helpers/statistics.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/helpers/statistics.py


class IStatisticsCollector(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    @property
    def update(self):
        raise NotImplementedError

    def needCollectSystemData(self, value):
        raise NotImplementedError

    def needCollectSessionData(self, value):
        raise NotImplementedError

    def getStatistics(self, andStop=True):
        raise NotImplementedError

    def getSessionData(self):
        raise NotImplementedError

    def noteHangarLoadingState(self, state, initialState=False, showSummaryNow=False):
        raise NotImplementedError

    def noteLastArenaData(self, arenaTypeID, arenaUniqueID, arenaTeam, randomEvents, blArenaPeriod):
        raise NotImplementedError
