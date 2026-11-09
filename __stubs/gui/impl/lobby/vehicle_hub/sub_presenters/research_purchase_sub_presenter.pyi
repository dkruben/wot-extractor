# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/research_purchase_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.game_control.links import URLMacros as URLMacros
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.research_purchase_model import ResearchPurchaseModel as ResearchPurchaseModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.vehicle_hub.sub_presenters.sub_presenter_base import SubPresenterBase as SubPresenterBase
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.events import VehicleBuyEvent as VehicleBuyEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showBlueprintView as showBlueprintView, selectVehicleInHangar as selectVehicleInHangar, showShop as showShop, showLootBoxEntry as showLootBoxEntry, showLootBoxBuyWindow as showLootBoxBuyWindow
from gui.shared.gui_items.gui_item_economics import getPriceTypeAndValue as getPriceTypeAndValue, ActualPrice as ActualPrice
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import ITradeInController as ITradeInController, IHeroTankController as IHeroTankController, IWalletController as IWalletController, IRestoreController as IRestoreController, ILootBoxSystemController as ILootBoxSystemController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.server_events.event_items import Action as Action

class ResearchPurchaseSubPresenter(SubPresenterBase):
    _restores: Any
    _tradeIn: Any
    _heroTanks: Any
    _wallet: Any
    _eventsCache: Any
    _lootBoxesCtrl: Any
    @property
    def viewModel(self):
        ...
    def initialize(self, vhCtx, *args, **kwargs):
        ...
    def setVehicleHubCtx(self, vhCtx):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def __fillViewModel(self):
        ...
    def __fillResearchPurchase(self, model):
        ...
    def __setActionState(self, actionState, actionStateReason, veh, vehPrice, currency, money, shop, info):
        ...
    @property
    def __isHeroTank(self):
        ...
    @property
    def __promo(self):
        ...
    # decorador original: @args2params(...)
    def __onAction(self, action):
        ...
    # decorador original: @adisp_process
    def __purchaseHeroTank(self):
        ...
    def __onShowBlueprint(self):
        ...
    def __onTradeInVehicleToSellSelected(self, _=None):
        ...
    def __onSyncCompleted(self, reason, diff):
        ...
    def __onWalletStatusChanged(self, *args):
        ...
    def __onRestoreChanged(self, vehicles):
        ...
    def __onLBStatusChanged(self):
        ...
