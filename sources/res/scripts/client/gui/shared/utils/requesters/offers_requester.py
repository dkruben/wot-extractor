# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/offers_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/offers_requester.py
from __future__ import absolute_import
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IOffersRequester

class OffersRequester(AbstractSyncDataRequester, IOffersRequester):

    def getReceivedGifts(self, offerID):
        return self.__getOffer(offerID).get('gifts', {})

    def isBannerSeen(self, offerID):
        return self.__getOffer(offerID).get('bannerSeen', False)

    def _requestCache(self, callback=None):
        BigWorld.player().offers.getCache((lambda resID, value: self._response(resID, value, callback)))

    def __getOffer(self, offerID):
        return self.getCacheValue('offersData', {}).get(offerID, {})
