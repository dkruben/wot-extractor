# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/skeletons/gui/game_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/skeletons/gui/game_control.py
from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Dict
    from Event import Event
    from comp7.gui.game_control.comp7_weekly_quests_controller import _Comp7WeeklyQuests
    from gui.ranked_battles.ranked_models import Rank

class IComp7ShopController(IGameController):
    onDataUpdated = None
    onShopStateChanged = None

    @property
    def isShopEnabled(self):
        raise NotImplementedError

    def getProducts(self):
        raise NotImplementedError

    def buyProduct(self, productCode):
        raise NotImplementedError

    def hasNewProducts(self, rank):
        raise NotImplementedError

    def hasNewDiscounts(self, newRank):
        raise NotImplementedError

    def validateCachedProducts(self):
        raise NotImplementedError


class IComp7WeeklyQuestsController(IGameController):
    onWeeklyQuestsUpdated = None

    def getQuests(self):
        raise NotImplementedError
