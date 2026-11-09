# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/badges_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/badges_requester.py
from __future__ import absolute_import
import typing, BigWorld
from gui.doc_loaders.badges_loader import getAvailableBadges
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBadgesRequester

class BadgesRequester(AbstractSyncDataRequester, IBadgesRequester):

    @property
    def available(self):
        return getAvailableBadges()

    @property
    def selected(self):
        return self.getCacheValue('badges', ())

    def _requestCache(self, callback=None):
        BigWorld.player().badges.getCache((lambda resID, value: self._response(resID, value, callback)))
