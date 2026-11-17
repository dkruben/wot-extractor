# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/shop_style_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from halloween.gui.impl.gen.view_models.views.lobby.widgets.shop_style_panel_model import ShopStylePanelModel as ShopStylePanelModel
from halloween.gui.shared.event_dispatcher import showHalloweenShopVehicle as showHalloweenShopVehicle
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.skeletons.halloween_shop_controller import IHalloweenShopController as IHalloweenShopController
from helpers import dependency as dependency
from items.vehicles import getVehicleType as getVehicleType, makeVehicleTypeCompDescrByName as makeVehicleTypeCompDescrByName
from skeletons.gui.shared import IItemsCache as IItemsCache
from halloween_common.configs.halloween_bestiary import EnemyModel as EnemyModel

# base nao representavel no stub: ViewComponent[...]
class ShopStylePanelPresenter:
    __hwCtrl: Any
    __hwBestiaryCtrl: Any
    __hwShopCtrl: Any
    __itemsCache: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    @staticmethod
    def __onClick():
        ...
    def __canPurchaseStyles(self, enemy):
        ...
    @staticmethod
    def __getVehName(enemy):
        ...
    def __update(self):
        ...
