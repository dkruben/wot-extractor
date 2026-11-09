# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/skeletons/gui/goodies.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/goodies.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional, Dict, List, Any, Tuple
    from gui.shared.money import Money
    from gui.shared.gui_items.fitting_item import FittingItem
    from gui.shared.utils.requesters.GoodiesRequester import GoodieVariable
    from gui.goodies.goodie_items import RecertificationForm, DemountKit, Booster, _PersonalDiscount, _Goodie
    from gui.shared.utils.requesters.ShopRequester import _ResourceData, _NamedGoodieData

class IBoostersStateProvider(object):

    @property
    def personalGoodies(self):
        raise NotImplementedError

    def getBoosters(self, criteria=None):
        raise NotImplementedError

    def getBooster(self, boosterID):
        raise NotImplementedError

    def getActiveResources(self):
        raise NotImplementedError

    def getActiveBoosterTypes(self):
        raise NotImplementedError

    def getBoosterPriceData(self, boosterID):
        raise NotImplementedError

    def isBoosterHiddenInShop(self, boosterID):
        raise NotImplementedError

    def haveBooster(self, boosterID):
        raise NotImplementedError

    def getClanReserves(self):
        raise NotImplementedError


class IGoodiesCache(IBoostersStateProvider):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def getItemByTargetValue(self, targetValue):
        raise NotImplementedError

    def getDiscount(self, discoutID):
        raise NotImplementedError

    def getDemountKit(self, demountKitID=None, currency=None):
        raise NotImplementedError

    def getGoodie(self, goodieID):
        raise NotImplementedError

    def getGoodieByID(self, goodieID):
        raise NotImplementedError

    def getDiscounts(self, criteria=None):
        raise NotImplementedError

    def getDemountKits(self, criteria=None):
        raise NotImplementedError

    def getRecertificationForm(self, recertificationFormID=None, currency=None):
        raise NotImplementedError

    def getRecertificationForms(self, criteria=None):
        raise NotImplementedError

    def getMentoringLicense(self, mentoringLicenseID=None, currency=None):
        raise NotImplementedError

    def getMentoringLicenses(self, criteria=None):
        raise NotImplementedError
