# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/stock.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import typing as typing
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from past.builtins import basestring as basestring
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.recruit_helper import getAllRecruitsInfo as getAllRecruitsInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.money import Money as Money
from gui.shared.utils.requesters.ItemsRequester import PredicateCondition as PredicateCondition, REQ_CRITERIA as REQ_CRITERIA, RequestCriteria as RequestCriteria
from helpers import dependency as dependency
from items import getTypeOfCompactDescr as getTypeOfCompactDescr
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, w2c as w2c
from web.web_client_api.common import ShopItemType as ShopItemType
from web.web_client_api.shop import formatters as formatters
from web.web_client_api.shop.crew import ShopCrewCriteria as ShopCrewCriteria, makeTankman as makeTankman
from typing import Optional as Optional, Set as Set
from gui.shared.gui_items.gui_item import GUIItem as GUIItem
_InventoryEnhancements: Any
_InstalledEnhancements: Any
_GUI_ITEMS_TYPE_MAP: dict
_ITEMS_CRITERIA_MAP: dict
ID_IN_LIST: Any
_SHOP_CUSTOMIZATION_TYPES: tuple
_SHOP_ITEM_TYPE_MAP: dict

class _PremiumPack(object):
    __duration: Any
    __price: Any
    def __init__(self, duration, cost, defCost):
        ...
    @property
    def id(self):
        ...
    @property
    def buyPrice(self):
        ...
    @property
    def duration(self):
        ...
    @property
    def userName(self):
        ...
    @property
    def shortDescriptionSpecial(self):
        ...
    @property
    def longDescriptionSpecial(self):
        ...

class IdInListCriteria(RequestCriteria):
    _conditions: Any
    def __call__(self, idList, itemType=None):
        ...

class _GetItemsByCdSchema(W2CSchema):
    cds: Any
    fields: Any

class _GetItemByCdSchema(W2CSchema):
    cd: Any
    fields: Any

class _GetItemsSchema(W2CSchema):
    type: Any
    criteria: Any
    fields: Any
    id_list: Any

class ItemsWebApiMixin(object):
    __itemsCache: Any
    __goodiesCache: Any
    __formattersMap: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def getItemsByCD(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getItemByCD(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getItems(self, cmd):
        ...
    def __getFormatter(self, itemType, criteria):
        ...
    def __makeFormatterKey(self, itemType, criteria):
        ...
    def __getItemByCD(self, cd, allowedFields=None):
        ...
    def __collectItems(self, itemType, criteria):
        ...
    def __collectBoosters(self, criteria):
        ...
    def __collectGuiItems(self, itemType, criteria):
        ...
    def __collectPremiumPacks(self):
        ...
    def __collectInventoryEnhancements(self):
        ...
    def __collectInstalledEnhancements(self):
        ...
    def __collectCrew(self, criteria):
        ...
    def __getCompatVehicles(self, itemType, itemID):
        ...
    def __getFittedVehicles(self, itemType, itemID):
        ...

def _parseCriteriaSpec(itemType, spec, idList=None):
    ...
