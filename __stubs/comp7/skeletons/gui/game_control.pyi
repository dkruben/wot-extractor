# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/skeletons/gui/game_control.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.game_control import IGameController as IGameController
from typing import Dict as Dict
from Event import Event as Event
from comp7.gui.game_control.comp7_weekly_quests_controller import _Comp7WeeklyQuests as _Comp7WeeklyQuests
from gui.ranked_battles.ranked_models import Rank as Rank

class IComp7ShopController(IGameController):
    onDataUpdated = None
    onShopStateChanged = None
    @property
    def isShopEnabled(self):
        ...
    def getProducts(self):
        ...
    def buyProduct(self, productCode):
        ...
    def hasNewProducts(self, rank):
        ...
    def hasNewDiscounts(self, newRank):
        ...
    def validateCachedProducts(self):
        ...

class IComp7WeeklyQuestsController(IGameController):
    onWeeklyQuestsUpdated = None
    def getQuests(self):
        ...
