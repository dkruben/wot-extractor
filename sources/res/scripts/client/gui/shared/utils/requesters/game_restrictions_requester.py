# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/game_restrictions_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/game_restrictions_requester.py
from __future__ import absolute_import
import typing, BigWorld
from constants import RESTRICTION_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGameRestrictionsRequester

class GameRestrictionsRequester(AbstractSyncDataRequester, IGameRestrictionsRequester):

    @property
    def session(self):
        return self.getCacheValue(RESTRICTION_KEY.SESSION) or {}

    @property
    def hasSessionLimit(self):
        return len(self.session) > 0

    def getKickAt(self):
        return self.session.get('kick_at', 0)

    @property
    def settings(self):
        return self.getCacheValue(RESTRICTION_KEY.SETTINGS) or {}

    @property
    def privateChat(self):
        return self.getCacheValue(RESTRICTION_KEY.PRIVATE_CHAT) or {}

    def _requestCache(self, callback=None):
        BigWorld.player().gameRestrictions.getCache((lambda resID, value: self._response(resID, value, callback)))
