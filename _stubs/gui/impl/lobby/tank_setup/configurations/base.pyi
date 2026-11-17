# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/configurations/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel as DealPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.setup_tab_model import SetupTabModel as SetupTabModel
from gui.impl.common.tabs_controller import TabsController as TabsController
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder as BuyPriceModelBuilder
from gui.shared.gui_items.fitting_item import canBuyWithGoldExchange as canBuyWithGoldExchange
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class BaseTankSetupTabsController(TabsController):
    __slots__: tuple
    _providers: Any
    def __init__(self, autoCreating=True):
        ...
    def getProvider(self, name):
        ...
    def _createViewModel(self, _):
        ...
    def _getAllProviders(self):
        ...

class BaseDealPanel(object):
    _itemsCache: Any
    _IN_STORAGE = 'inStorage'
    _ON_VEHICLE_IN_SETUP = 'inSetup'
    _MONEY = 'money'
    @classmethod
    def updateDealPanelPrice(cls, vehicle, items, dealPanelModel):
        ...
    @classmethod
    def updateAutoRenewalState(cls, interactor, dealPanelModel):
        ...
    @classmethod
    def addItem(cls, vehicle, item, prices):
        ...
    @classmethod
    def removeItem(cls, item, prices):
        ...
    @classmethod
    def _updateDisabled(cls, prices, dealPanelModel):
        ...
