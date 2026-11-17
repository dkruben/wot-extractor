# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/easy_tank_equip_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from collections import OrderedDict as OrderedDict
from BWUtil import AsyncReturn as AsyncReturn
from typing import TYPE_CHECKING as TYPE_CHECKING, NamedTuple as NamedTuple, Type as Type
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.SystemMessages import pushMessagesFromResult as pushMessagesFromResult
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalType as ProposalType, ProposalModel as ProposalModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.easy_tank_equip_view_model import EasyTankEquipViewModel as EasyTankEquipViewModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.easy_tank_equip.cards.base_card import BaseCard as BaseCard
from gui.impl.lobby.easy_tank_equip.cards.consumables_card import ConsumablesCard as ConsumablesCard
from gui.impl.lobby.easy_tank_equip.cards.crew_card import CrewCard as CrewCard
from gui.impl.lobby.easy_tank_equip.cards.opt_devices_card import OptDevicesCard as OptDevicesCard
from gui.impl.lobby.easy_tank_equip.cards.shells_card import ShellsCard as ShellsCard
from gui.impl.lobby.easy_tank_equip.cards.styles_card import StylesCard as StylesCard
from gui.impl.lobby.easy_tank_equip.data_providers.consumables_data_provider import ConsumablesDataProvider as ConsumablesDataProvider
from gui.impl.lobby.easy_tank_equip.data_providers.crew_data_provider import CrewDataProvider as CrewDataProvider
from gui.impl.lobby.easy_tank_equip.data_providers.opt_devices_data_provider import OptDevicesDataProvider as OptDevicesDataProvider
from gui.impl.lobby.easy_tank_equip.data_providers.shells_data_provider import ShellsDataProvider as ShellsDataProvider
from gui.impl.lobby.easy_tank_equip.data_providers.styles_data_provider import StylesDataProvider as StylesDataProvider
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_deal_panel import EasyTankEquipBottomContent as EasyTankEquipBottomContent
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_vehicle import g_easyTankEquipCopyVehicle as g_easyTankEquipCopyVehicle
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import EasyTankEquipParamsPresenter as EasyTankEquipParamsPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import event_dispatcher as shared_events
from gui.shared.close_confiramtor_helper import CloseConfirmatorsHelper as CloseConfirmatorsHelper
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.gui_items.processors.vehicle import EasyTankEquipApplyProcessor as EasyTankEquipApplyProcessor
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.money import Currency as Currency, ZERO_MONEY as ZERO_MONEY
from gui.shared.tooltips.contexts import EasyTankEquipParamContext as EasyTankEquipParamContext
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IEasyTankEquipController as IEasyTankEquipController
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.easy_tank_equip.loggers import EasyTankEquipLogger as EasyTankEquipLogger, LOGGING_ITEMS_MAP as LOGGING_ITEMS_MAP
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.lobby.easy_tank_equip.data_providers.base_data_provider import BaseDataProvider as BaseDataProvider
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from typing import List as List, Optional as Optional
_logger: Any
PROVIDERS_PRIORITIES_MAP: Any
GUI_ITEM_TYPE_TO_PROPOSAL_MAP: dict
CardInfo: Any

class _EasyTankEquipCloseConfirmatorsHelper(CloseConfirmatorsHelper):
    def start(self, closeConfirmator):
        ...
    def stop(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class EasyTankEquipPresenter:
    __appLoader: Any
    __easyTankEquipCtrl: Any
    __itemsCache: Any
    __closeConfirmatorHelper: Any
    __bottomContent: Any
    __vehicleParamsView: Any
    __cards: Any
    __providers: Any
    __isApplyInProcess: Any
    __isApplyBtnClicked: Any
    __uiLogger: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def copyVehicle(self):
        ...
    def createToolTip(self, event):
        ...
    def onEntered(self):
        ...
    def onExit(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __getCardsLogInfo(self):
        ...
    def __createSpecialTooltip(self, tooltipId, specialArgs):
        ...
    def __initializeProviders(self):
        ...
    def __initializeCards(self):
        ...
    def __initializeBottomContent(self):
        ...
    def __finalizeCards(self):
        ...
    def __finalizeProviders(self):
        ...
    def __finalizeBottomContent(self):
        ...
    def __onSettingsChange(self):
        ...
    def __onItemsCacheSyncCompleted(self, reason, diff):
        ...
    def __onMoneyUpdated(self, _):
        ...
    def __updateCardsBalances(self):
        ...
    def __updateDealPanelPrices(self):
        ...
    def __updateTTC(self):
        ...
    def __onClose(self):
        ...
    def __clearProposal(self):
        ...
    def __clear(self):
        ...
    # decorador original: @args2params(...)
    def __onSelectProposal(self, proposalType):
        ...
    # decorador original: @args2params(...)
    def __onSwitchPreset(self, proposalType, presetIndex):
        ...
    # decorador original: @args2params(...)
    def __onSwapSlots(self, proposalType, firstSlot, secondSlot, isDndUsed):
        ...
    # decorador original: @wg_async
    def __onDealPanelConfirmed(self):
        ...
    def __onDealPanelCancelled(self):
        ...
    def __update(self):
        ...
    def __onInventoryUpdate(self, diff):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __apply(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __applyEasyTankEquipPresets(self, data, callback):
        ...
    def __applyCrew(self, crew):
        ...
    def __getPresetsDataForApplying(self):
        ...
    def __getCrewPresetDataForApplying(self):
        ...
    def __saveAccountSettings(self):
        ...
    # decorador original: @wg_async
    def __onExit(self):
        ...
    # decorador original: @wg_async
    def __closeConfirmator(self):
        ...
