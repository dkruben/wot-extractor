# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tech_tree/tech_tree_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from logging import getLogger as getLogger
import typing as typing
import Event as Event
import nations as nations
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NATIONS_VISITED as NATIONS_VISITED
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver, visitor as visitor
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getPremiumVehiclesUrl as getPremiumVehiclesUrl
from gui.Scaleform.daapi.view.lobby.techtree import dumpers as dumpers
from gui.Scaleform.daapi.view.lobby.techtree.data import NationTreeData as NationTreeData
from gui.Scaleform.daapi.view.lobby.techtree.listeners import TTListenerDecorator as TTListenerDecorator
from gui.Scaleform.daapi.view.lobby.techtree.settings import NODE_STATE as NODE_STATE
from gui.Scaleform.daapi.view.lobby.techtree.settings import SelectedNation as SelectedNation
from gui.Scaleform.daapi.view.lobby.techtree.sound_constants import TECHTREE_SOUND_SPACE as TECHTREE_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.techtree.states import TechtreeState as TechtreeState
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS as NODE_STATE_FLAGS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.backport import BackportContextMenuWindow as BackportContextMenuWindow, createContextMenuData as createContextMenuData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tech_tree.tech_tree_view_model import TechTreeViewModel as TechTreeViewModel, NationEnum as NationEnum
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.lobby.hangar.presenters.utils import GUINode as GUINode
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_dispatcher import showVehicleHubModules as showVehicleHubModules
from gui.shared.utils.vehicle_collector_helper import hasCollectibleVehicles as hasCollectibleVehicles
from gui.sounds.ambients import LobbySubViewEnv as LobbySubViewEnv
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from typing import Tuple as Tuple, List as List, Set as Set, Dict as Dict, Optional as Optional
from gui.Scaleform.daapi.view.lobby.techtree.settings import UnlockProps as UnlockProps
from gui.Scaleform.daapi.view.lobby.techtree.nodes import RealNode as RealNode
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from frameworks_common.state_machine import State as State
from gui.shared.events import NavigationEvent as NavigationEvent
_logger: Any
_VEHICLE_URL_FILTER_PARAM = 1

class _NationTreeViewDumper(dumpers._BaseDumper):
    def __init__(self, cache=None):
        ...
    def clear(self, full=False):
        ...
    def dump(self, data):
        ...
    def _getTechTreeNodes(self, node, nodeRows):
        ...
    def _getNodeOverrides(self, node):
        ...

class _TechTreeStatesObserver(BaseStateObserver):
    onSwitchNation: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...

class TechTreeView(ViewImpl, IRoutableView):
    __lobbyContext: Any
    __cmpBasket: Any
    __sound_env__ = LobbySubViewEnv
    _COMMON_SOUND_SPACE = TECHTREE_SOUND_SPACE
    __ctx: Any
    __nationTreeData: Any
    __techTreeStatesObserver: Any
    __listener: Any
    __router: Any
    def __init__(self, layoutID, ctx=None):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @property
    def viewModel(self):
        ...
    def getRouterModel(self):
        ...
    def redraw(self):
        ...
    def createToolTip(self, event):
        ...
    def createContextMenu(self, event):
        ...
    def _getEvents(self):
        ...
    def __onInitNation(self, args):
        ...
    # decorador original: @args2params(...)
    def __onSwitchNation(self, nation):
        ...
    # decorador original: @args2params(...)
    def __onOpenAboutVehicle(self, vehCD, route):
        ...
    # decorador original: @args2params(...)
    def __onAddToCompare(self, vehCD):
        ...
    # decorador original: @args2params(...)
    def __onOpenCollectableVehicles(self, nation):
        ...
    # decorador original: @args2params(...)
    def __onOpenPremiumShop(self, nation, level):
        ...
    def __getCollectableVehiclesSate(self):
        ...
    def __fullUpdateOfViewModel(self):
        ...
    def __fillTechTreeNodes(self, vm, techTreeNodesDump):
        ...
    def __fillNodeOverrides(self, vm, nodeOverridesDump):
        ...
    def __updateAllNodeOverrides(self):
        ...
    def __updateCollectableVehiclesState(self):
        ...
    def __updateNodeOverrides(self, nodesToUpdate):
        ...
    def __invalidateAllCurrencies(self):
        ...
    def invalidateBlueprintMode(self, isEnabled):
        ...
    def invalidateVehLocks(self, locks):
        ...
    def invalidateVTypeXP(self, xps):
        ...
    def invalidateWalletStatus(self, status):
        ...
    def invalidateRent(self, vehicles):
        ...
    def invalidateRestore(self, vehicles):
        ...
    def invalidateBlueprints(self, blueprints):
        ...
    def invalidateVehicleCollectorState(self):
        ...
    def invalidateCredits(self):
        ...
    def invalidateGold(self):
        ...
    def invalidateFreeXP(self):
        ...
    def invalidateElites(self, elites):
        ...
    def invalidateUnlocks(self, unlocks):
        ...
    def invalidateInventory(self, data):
        ...
    def invalidatePrbState(self):
        ...
    def invalidateDiscounts(self, data):
        ...
    def invalidateVehCompare(self):
        ...
    def invalidateVehPostProgression(self):
        ...
    def clearSelectedNation(self):
        ...

class TechTreeWindow(WindowImpl):
    __background_alpha__: Any
    def __init__(self, layer, **kwargs):
        ...

def _getVehCDs(invalidationResult):
    ...
