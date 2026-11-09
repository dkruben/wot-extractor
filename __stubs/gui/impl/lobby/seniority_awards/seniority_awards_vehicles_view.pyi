# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_vehicles_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from BWUtil import AsyncReturn as AsyncReturn
from constants import ROLE_TYPE as ROLE_TYPE
from frameworks.wulf import ViewSettings as ViewSettings, WindowLayer as WindowLayer
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.game_control.seniority_awards_controller import VehicleSelectionState as VehicleSelectionState, VehiclesForSelectionState as VehiclesForSelectionState, SELECT_REWARD_TIMEOUT as SELECT_REWARD_TIMEOUT
from gui.impl import backport as backport
from gui.impl.auxiliary.rewards_helper import getRewardTooltipContent as getRewardTooltipContent, getSeniorityAwardsVehicles as getSeniorityAwardsVehicles
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_awards_tooltip_constants import SeniorityAwardsTooltipConstants as SeniorityAwardsTooltipConstants
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_awards_vehicle_model import SeniorityAwardsVehicleModel as SeniorityAwardsVehicleModel
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_awards_vehicles_view_model import SeniorityAwardsVehiclesViewModel as SeniorityAwardsVehiclesViewModel, ViewState as ViewState
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.platoon.platoon_helpers import removeNationFromTechName as removeNationFromTechName
from gui.impl.lobby.seniority_awards.seniority_awards_helper import getVehicleCD as getVehicleCD, showVehicleSelectionTimeoutError as showVehicleSelectionTimeoutError, showVehicleSelectionMultipleTokensError as showVehicleSelectionMultipleTokensError, getRewardCategoryForUI as getRewardCategoryForUI
from gui.impl.lobby.seniority_awards.seniority_awards_sounds import SENIORITY_REWARD_SOUND_SPACE as SENIORITY_REWARD_SOUND_SPACE
from gui.impl.lobby.seniority_awards.tooltip.seniority_awards_tooltip import SeniorityAwardsTooltip as SeniorityAwardsTooltip
from gui.impl.lobby.tooltips.vehicle_role_descr_view import VehicleRolesTooltipView as VehicleRolesTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers import dependency as dependency
from skeletons.gui.game_control import ISeniorityAwardsController as ISeniorityAwardsController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.seniority_awards.loggers import VehicleSelectionErrorNotificationsLogger as VehicleSelectionErrorNotificationsLogger
from wg_async import wg_async as wg_async, wg_await as wg_await, BrokenPromiseError as BrokenPromiseError, AsyncScope as AsyncScope, AsyncEvent as AsyncEvent, TimeoutError as TimeoutError
_logger: Any
_SENIORITY_VEHICLES_ORDER: tuple

class SeniorityRewardVehiclesView(ViewImpl):
    _COMMON_SOUND_SPACE = SENIORITY_REWARD_SOUND_SPACE
    __itemsCache: Any
    __lobbyContext: Any
    __seniorityAwardsCtrl: Any
    __eventsCache: Any
    __vehicles: Any
    __selectedVehicleId: Any
    __state: Any
    __scope: Any
    __vehicleSelectionQuestCompletedEvent: Any
    __vehicleSelectionQuestId: Any
    def __init__(self, contentResId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @wg_async
    def __selectVehicleReward(self, vehicleRewardId):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, vehicles, fromEntryPoint, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def __onQuestsReceived(self, *_, **__):
        ...
    def __setRewards(self, viewModel):
        ...
    def __setAvailableVehicles(self, viewModel):
        ...
    def __getBackportTooltipData(self, event):
        ...
    def __updateVehicles(self, vehicles):
        ...
    def __handleOnMoreRewards(self):
        ...
    def __handleShowHangar(self):
        ...
    # decorador original: @wg_async
    def __handleOnSelectVehicleReward(self, event):
        ...
    def __handleOnClose(self):
        ...
    @staticmethod
    def __showWaiting():
        ...
    @staticmethod
    def __hideWaiting():
        ...
    def __updateModelAfterSelection(self):
        ...
    def __onSettingsChange(self):
        ...
    def __onVehicleForSelectionChanged(self):
        ...
    def __onVehicleSelectionChanged(self, state):
        ...

class SeniorityRewardVehiclesWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, viewID=None, vehicles=None, fromEntryPoint=True):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _vehiclesSortOrder(vehicleCD, itemsCache=None):
    ...
def _sortVehiclesDict(vehDictItem):
    ...
