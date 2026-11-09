# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/EpicMetaGameRequester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/EpicMetaGameRequester.py
from __future__ import absolute_import, division
import typing
from past.utils import old_div
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IEpicMetaGameRequester

class EpicMetaGameRequester(AbstractSyncDataRequester, IEpicMetaGameRequester):

    @property
    def playerLevelInfo(self):
        return self.getCacheValue('metaLevel', (1, 0))

    @property
    def seasonData(self):
        return self.getCacheValue('seasonData', (0, None, {}))

    @property
    def skillPoints(self):
        return self.getCacheValue('abilityPts', 0)

    def selectedSkills(self, vehicleCD):
        skillsDict = self.getCacheValue('selectedAbilities', None)
        if skillsDict is not None:
            return skillsDict.get(vehicleCD, [])
        else:
            return []

    @property
    def skillLevels(self):
        return self.getCacheValue('abilities', {})

    @property
    def battleCount(self):
        return self.getCacheValue('battleCount', 0)

    @property
    def averageXP(self):
        if self.battleCount > 0:
            return old_div(self.getCacheValue('famePts', 0), self.battleCount)
        return 0

    def _requestCache(self, callback=None):
        BigWorld.player().epicMetaGame.getCache((lambda resID, value: self._response(resID, value, callback)))

    def _preprocessValidData(self, data):
        if 'epicMetaGame' in data:
            return dict(data['epicMetaGame'])
        return {}
