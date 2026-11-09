# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/wrappers/user_compound_price_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import iteritems as iteritems
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.compound_price_model import CompoundPriceModel as CompoundPriceModel
from gui.impl.gen.view_models.common.price_model import PriceModel as PriceModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel
from gui.shared.money import Money as Money
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Tuple as Tuple, Optional as Optional, Union as Union, Iterable as Iterable
_logger: Any
Price: Any

class UserCompoundPriceModel(CompoundPriceModel):
    __slots__: tuple
    def clear(self):
        ...
    def assign(self, *itemPrices):
        ...

class PriceModelBuilder(object):
    @classmethod
    def getPriceModel(cls, price, action=None, defPrice=None):
        ...
    @classmethod
    def clearPriceModel(cls, priceModel):
        ...
    @classmethod
    def fillPriceModelByItemPrice(cls, priceModel, itemPrice, checkBalanceAvailability=False, priceID=''):
        ...
    @classmethod
    def fillPriceModel(cls, priceModel, price, action=None, defPrice=None, checkBalanceAvailability=False, priceID=''):
        ...
    @classmethod
    def fillPriceItemModel(cls, array, price, checkBalanceAvailability=False):
        ...
    @classmethod
    def _createPriceItemModel(cls, name, value, _=False):
        ...
    @classmethod
    def _getCurrencyIterator(cls, price):
        ...

class BuyPriceModelBuilder(PriceModelBuilder):
    _itemsCache: Any
    @classmethod
    def fillPriceModel(cls, priceModel, price, action=None, defPrice=None, checkBalanceAvailability=False, priceID='', balance=None):
        ...
    @classmethod
    def fillPriceItemModel(cls, array, price, balance=None, checkBalanceAvailability=False):
        ...
    @classmethod
    def _createPriceItemModel(cls, name, value, balance=None, checkBalanceAvailability=False):
        ...
