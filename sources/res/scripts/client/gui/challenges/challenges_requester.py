# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/challenges/challenges_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/challenges/challenges_requester.py
from __future__ import absolute_import
import BigWorld
from challenges_common import CHALLENGES_PDATA_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IChallengesRequester

class ChallengesRequester(AbstractSyncDataRequester, IChallengesRequester):

    def getUsedFreeRestarts(self, challengeID):
        return self.getCacheValue(challengeID, {}).get('restartsUsed', 0)

    def _preprocessValidData(self, data):
        return dict(data.get(CHALLENGES_PDATA_KEY, {}))

    def _requestCache(self, callback=None):
        BigWorld.player().challenges.getCache((lambda resID, value: self._response(resID, value, callback)))
