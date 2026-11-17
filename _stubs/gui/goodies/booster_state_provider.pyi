# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/goodies/booster_state_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import logging as logging
import BigWorld as BigWorld
from Event import Event as Event
from gui.goodies.goodie_items import Booster as Booster
from gui.shared.money import Money as Money
from goodies.goodie_constants import GOODIE_STATE as GOODIE_STATE, GOODIE_VARIETY as GOODIE_VARIETY, GOODIE_TARGET_TYPE as GOODIE_TARGET_TYPE, PR2BoosterIDs as PR2BoosterIDs
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.requesters.GoodiesRequester import GoodieVariable as GoodieVariable
from gui.shared.utils.requesters.ShopRequester import _NamedGoodieData as _NamedGoodieData
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from helpers.time_utils import getServerTimeDiffInLocal as getServerTimeDiffInLocal
from skeletons.gui.goodies import IBoostersStateProvider as IBoostersStateProvider
from typing import Dict as Dict, Any as Any, Optional as Optional, List as List, Tuple as Tuple, Union as Union
from gui.shared.utils.requesters.ShopRequester import _ResourceData as _ResourceData
from goodies.goodie_constants import GOODIE_RESOURCE_TYPE as GOODIE_RESOURCE_TYPE
_logger: _Any

class BoosterStateProvider(IBoostersStateProvider):
    __personalGoodies: _Any
    __activeResources: _Any
    __boosters: _Any
    __activeBoosterTypes: _Any
    __notificationManager: _Any
    onStateUpdated: _Any
    def __init__(self):
        ...
    @property
    def personalGoodies(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAvatarBecomeNonPlayer(self):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def getBoosters(self, criteria=None):
        ...
    def getBooster(self, boosterId):
        ...
    def getClanReserves(self):
        ...
    def getActiveResources(self):
        ...
    def getActiveBoosterTypes(self):
        ...
    def isBoosterHiddenInShop(self, boosterID):
        ...
    def haveBooster(self, boosterID):
        ...
    def addBooster(self, bID, booster, stateInfo, resourceData):
        ...
    def getBoosterPriceData(self, boosterID):
        ...
    def buildCache(self):
        ...
    def _filterOutExpired(self, stateInfo):
        ...
    def _timeTillNextNotification(self):
        ...
