# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/e_sport/unit/public/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.entities.base.cooldown import PrbCooldownManager as PrbCooldownManager
from gui.prb_control.entities.base.requester import IPrbListRequester as IPrbListRequester
from gui.prb_control.items.unit_seqs import UnitsListIterator as UnitsListIterator, UnitsUpdateIterator as UnitsUpdateIterator
from gui.prb_control.settings import REQUEST_TYPE as REQUEST_TYPE
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class UnitsListRequester(IPrbListRequester):
    itemsCache: Any
    __selectedID: Any
    __callback: Any
    __callbackUpdate: Any
    __isSubscribed: Any
    __cooldown: Any
    __handlers: Any
    __cache: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    def start(self, callback):
        ...
    def stop(self):
        ...
    def request(self, **kwargs):
        ...
    def subscribe(self, unitTypeFlags):
        ...
    def unsubscribe(self):
        ...
    def setSelectedID(self, selectedID):
        ...
    def addCacheItem(self, item):
        ...
    def getCacheItem(self, cfdUnitID):
        ...
    def removeCacheItem(self, cfdUnitID):
        ...
    def __navLeft(self, browser, **kwargs):
        ...
    def __navRight(self, browser, **kwargs):
        ...
    def __recenter(self, browser, **kwargs):
        ...
    def __refresh(self, browser, **kwargs):
        ...
    def __unitBrowser_onUnitsListReceived(self, data):
        ...
    def __unitBrowser_onUnitsListUpdated(self, data):
        ...
