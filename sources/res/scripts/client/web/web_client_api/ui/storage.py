# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/storage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/storage.py
from __future__ import absolute_import
from past.builtins import basestring
from gui.Scaleform.daapi.view.lobby.storage import getSectionsList, STORAGE_CONSTANTS
from gui.shared import event_dispatcher as shared_events
from helpers import dependency
from skeletons.gui.offers import IOffersDataProvider
from web.web_client_api import w2c, W2CSchema, Field, WebCommandException

def _validateSection(value, _):
    if value in (section['id'] for section in getSectionsList()):
        return True
    raise WebCommandException(value)


class _OpenStorageSchema(W2CSchema):
    section_id = Field(required=False, type=basestring, validator=_validateSection)


class _OpenOfferSchema(W2CSchema):
    offer_id = Field(required=True, type=int)


class StorageWebApiMixin(object):
    _offersProvider = dependency.descriptor(IOffersDataProvider)

    @w2c(_OpenStorageSchema, 'storage')
    def openStorage(self, cmd):
        sectionId = cmd.section_id
        if sectionId is not None:
            shared_events.showStorage(sectionId)
        else:
            shared_events.showStorage()
        return

    @w2c(_OpenOfferSchema, 'offer')
    def openOffer(self, cmd):
        offerId = cmd.offer_id
        offer = self._offersProvider.getOffer(offerId)
        if offer:
            shared_events.showOfferGiftsWindow(offerId)
        else:
            shared_events.showStorage(STORAGE_CONSTANTS.OFFERS)
