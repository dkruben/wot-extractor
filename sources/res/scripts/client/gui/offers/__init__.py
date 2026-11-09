# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/offers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/offers/__init__.py
from gui.offers.offers_banner_controller import OffersBannerController
from gui.offers.data_provider import OffersDataProvider
from gui.offers.offers_novelty import OffersNovelty
from skeletons.gui.offers import IOffersNovelty, IOffersBannerController, IOffersDataProvider

def getOffersConfig(manager):

    def _create():
        instance = OffersNovelty()
        instance.init()
        return instance

    manager.addRuntime(IOffersNovelty, _create, finalizer='fini')
    offersPrv = OffersDataProvider()
    offersPrv.init()
    manager.addInstance(IOffersDataProvider, offersPrv, finalizer='fini')
    bannerCtrl = OffersBannerController()
    bannerCtrl.init()
    manager.addInstance(IOffersBannerController, bannerCtrl, finalizer='fini')
