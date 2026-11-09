# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/battle_pass_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/battle_pass_requester.py
from __future__ import absolute_import
import BigWorld
from battle_pass_common import BATTLE_PASS_PDATA_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBattlePassRequester

class BattlePassRequester(AbstractSyncDataRequester, IBattlePassRequester):

    def getSeasonID(self):
        return self.getCacheValue('seasonID', 0)

    def getState(self):
        return self.getCacheValue('state', 0)

    def getActiveChapterID(self):
        return self.getCacheValue('chapterID', 0)

    def getPointsForVehicle(self, vehicleID, default=0):
        return self.getCacheValue('vehiclePoints', {}).get(vehicleID, default)

    def getChapterStats(self):
        return self.getCacheValue('seasonStats', {}).get('chaptersStats', {})

    def getCurrentLevelByChapterID(self, chapterID):
        return self.getChapterStats().get(chapterID, {}).get('level', 0)

    def getPointsByChapterID(self, chapterID):
        return self.getChapterStats().get(chapterID, {}).get('points', 0)

    def getNonChapterPoints(self):
        return self.getCacheValue('seasonStats', {}).get('nonChapterPoints', 0)

    def _preprocessValidData(self, data):
        return dict(data.get(BATTLE_PASS_PDATA_KEY, {}))

    def _requestCache(self, callback=None):
        BigWorld.player().battlePass.getCache((lambda resID, value: self._response(resID, value, callback)))
