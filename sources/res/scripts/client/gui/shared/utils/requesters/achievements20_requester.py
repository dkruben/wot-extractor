# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/achievements20_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/achievements20_requester.py
from __future__ import absolute_import
import typing, BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IAchievements20Requester
from constants import AchievementsLayoutStates
if typing.TYPE_CHECKING:
    from typing import List

class Achievements20Requester(AbstractSyncDataRequester, IAchievements20Requester):

    def getLayout(self):
        return self.getCacheValue('achievementsLayout', {}).get('layout', [])

    def getLayoutState(self):
        return self.getCacheValue('achievementsLayout', {}).get('state', AchievementsLayoutStates.AUTO)

    def getAchievementBitmask(self):
        return self.getCacheValue('achievementsLayout', {}).get('achievementBitmask', AchievementsLayoutStates.AUTO)

    def getLayoutLength(self):
        return self.getCacheValue('achievementsLayout', {}).get('layoutLength', 0)

    def _preprocessValidData(self, data):
        return dict(data.get('achievements20', {}))

    def _requestCache(self, callback=None):
        BigWorld.player().achievements20.getCache((lambda resID, value: self._response(resID, value, callback)))
