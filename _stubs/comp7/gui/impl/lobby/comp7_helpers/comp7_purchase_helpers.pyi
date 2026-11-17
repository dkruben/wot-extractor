# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_purchase_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import ProductState as ProductState, ProductTypes as ProductTypes
from comp7.gui.impl.gen.view_models.views.lobby.reward_product_model import RewardProductModel as RewardProductModel
from comp7.gui.impl.gen.view_models.views.lobby.style3d_product_model import Style3dProductModel as Style3dProductModel
from comp7.gui.impl.gen.view_models.views.lobby.vehicle_product_model import VehicleProductModel as VehicleProductModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getStylePreviewVehicle as getStylePreviewVehicle
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.shared.economics import getGUIPrice as getGUIPrice
from helpers import dependency as dependency
from items import ITEM_TYPES as ITEM_TYPES, parseIntCompactDescr as parseIntCompactDescr
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from typing import Union as Union, Type as Type
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.customization.c11n_items import Style as Style
T_PRODUCT_MODEL: Any
T_PRODUCT_MODEL_TYPE: Any

class _BaseProductPacker(object):
    __slots__: tuple
    _itemsCache: Any
    __tradeInController: Any
    __itemCD: Any
    def __init__(self, itemCD):
        ...
    @property
    def _productModel(self):
        ...
    @property
    def _productType(self):
        ...
    def pack(self, price):
        ...
    def _setProductSpecificData(self, item, productModel):
        ...
    def __getState(self, item):
        ...
    def __setPriceModelData(self, item, price, priceModel):
        ...
    def __setRestorePrice(self, item, priceModel):
        ...
    def __setProductPrice(self, price, priceModel):
        ...

class _VehiclePacker(_BaseProductPacker):
    @property
    def _productModel(self):
        ...
    @property
    def _productType(self):
        ...
    def _setProductSpecificData(self, item, productModel):
        ...

class _StylePacker(_BaseProductPacker):
    @property
    def _productModel(self):
        ...
    @property
    def _productType(self):
        ...
    def _setProductSpecificData(self, item, productModel):
        ...

class _OptionalDevicePacker(_BaseProductPacker):
    @property
    def _productModel(self):
        ...
    @property
    def _productType(self):
        ...

def getComp7ProductModel(itemCD, price):
    ...
def getItemType(itemCD):
    ...
