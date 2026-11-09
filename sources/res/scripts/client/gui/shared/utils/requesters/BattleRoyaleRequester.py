# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/BattleRoyaleRequester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/BattleRoyaleRequester.py
from __future__ import absolute_import
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBattleRoyaleRequester

class BattleRoyaleRequester(AbstractSyncDataRequester, IBattleRoyaleRequester):

    @property
    def accTitle(self):
        return self.getCacheValue('accBRTitle', (1, 0))

    @property
    def battleCount(self):
        return self.getCacheValue('BRBattlesCount', 0)

    @property
    def killCount(self):
        return self.getCacheValue('BRTotalKills', 0)

    @property
    def topCount(self):
        return self.getCacheValue('BRSoloTop1Count') + self.getCacheValue('BRSquadTop1Count')

    @property
    def dailyBonusUsedVehicles(self):
        return self.getCacheValue('brBattleStats', {}).get('dailyBonusUsedVehs', set())

    def getStats(self, arenaBonusType, playerDatabaseID=None):
        if playerDatabaseID:
            return {}
        return self.getCacheValue('brBattleStats').get(arenaBonusType, {})

    def _requestCache(self, callback=None):
        BigWorld.player().battleRoyale.getCache((lambda resID, value: self._response(resID, value, callback)))

    def _preprocessValidData(self, data):
        if 'battleRoyale' in data:
            return dict(data['battleRoyale'])
        return {}
