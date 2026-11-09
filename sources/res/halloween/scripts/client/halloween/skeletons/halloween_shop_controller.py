# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/skeletons/halloween_shop_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/skeletons/halloween_shop_controller.py
from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class IHalloweenShopController(IGameController):
    onShopSettingsUpdated = None
    onBundlesUpdated = None

    def isEnabled(self):
        raise NotImplementedError

    def keyBundles(self):
        raise NotImplementedError

    def getBundleByID(self, bundleID):
        raise NotImplementedError

    def getKeysInBundle(self, bundleID):
        raise NotImplementedError

    def purchaseBundle(self, bundleID, int):
        raise NotImplementedError

    def getPurchaseCount(self, bundleID):
        raise NotImplementedError

    def hasNotPurchasedBundles(self):
        raise NotImplementedError

    def checkIsEnoughBundles(self):
        raise NotImplementedError
