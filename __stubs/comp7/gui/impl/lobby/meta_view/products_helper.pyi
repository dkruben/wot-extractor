# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/products_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from account_helpers.AccountSettings import AccountSettings as AccountSettings, COMP7_UI_SECTION as COMP7_UI_SECTION, COMP7_SHOP_SEEN_PRODUCTS as COMP7_SHOP_SEEN_PRODUCTS
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import BaseProductModel as BaseProductModel, ProductTypes as ProductTypes, ProductState as ProductState
from comp7.gui.impl.gen.view_models.views.lobby.reward_product_model import RewardProductModel as RewardProductModel
from comp7.gui.impl.gen.view_models.views.lobby.style3d_product_model import Style3dProductModel as Style3dProductModel
from comp7.gui.impl.gen.view_models.views.lobby.vehicle_product_model import VehicleProductModel as VehicleProductModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import getComp7BonusPacker as getComp7BonusPacker
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getStylePreviewVehicle as getStylePreviewVehicle
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import getCDFromId as getCDFromId
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.server_events.bonuses import ItemsBonus as ItemsBonus
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from items.vehicles import g_cache as g_cache
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from comp7.gui.game_control.comp7_shop_controller import ShopPageProductInfo as ShopPageProductInfo
_PRODUCT_TYPE_TO_MODEL: dict
_PRODUCT_TYPE_ORDER: list
_COMP7_PREV_SEASON_PRODUCTS: set

def packProduct(productData):
    ...
def setProductModelData(productData, productModel):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getItemType(intCD, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehicleCDAndStyle(cd, c11nService=None):
    ...
def getSeenProducts():
    ...
def addSeenProduct(product):
    ...
def hasUnseenProduct(products):
    ...
def _getProductTypeData(product):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _setGenericData(model, productCD, productType, product, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getProductState(productCD, purchaseAllowed, isPersonalLimitsReached, itemsCache=None):
    ...
def _setSpecificData(model, productCD, productType):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _setVehicleSpecificData(model, productCD, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _setStyleSpecificData(model, productCD, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _setRewardSpecificData(model, productCD, itemsCache=None):
    ...
