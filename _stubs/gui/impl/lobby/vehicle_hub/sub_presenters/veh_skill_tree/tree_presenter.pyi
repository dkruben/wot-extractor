# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/veh_skill_tree/tree_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.shared.lock_overlays import lockNotificationManager as lockNotificationManager
from wg_async import wg_async as wg_async
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import VEH_SKILL_TREE_HINT_SHOWN as VEH_SKILL_TREE_HINT_SHOWN, VEH_SKILL_TREE_PRESTIGE_GLARE_SHOWN as VEH_SKILL_TREE_PRESTIGE_GLARE_SHOWN
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from frameworks.wulf import Array as Array
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.lobby.vehicle_hub import VehicleHubCtx as VehicleHubCtx, VehSkillTreeProgressionState as VehSkillTreeProgressionState
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.presenter_location_controller import IPresenterLocationController as IPresenterLocationController
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.utils import fillNodeModel as fillNodeModel, getEliteExpirience as getEliteExpirience, constructNodeUiId as constructNodeUiId, deconstructNodeUiId as deconstructNodeUiId
from gui.impl.lobby.veh_skill_tree.tooltips.final_perk_tooltip import FinalPerkTooltipView as FinalPerkTooltipView
from gui.impl.lobby.veh_skill_tree.tooltips.common_perk_tooltip import CommonPerkTooltipView as CommonPerkTooltipView
from gui.impl.lobby.veh_skill_tree.tooltips.major_perk_tooltip import MajorPerkTooltipView as MajorPerkTooltipView
from gui.impl.lobby.veh_skill_tree.tooltips.special_perk_tooltip import SpecialPerkTooltipView as SpecialPerkTooltipView
from gui.impl.gui_decorators import args2params as args2params
from gui.shared.event_dispatcher import showAlternateConfigurationDialog as showAlternateConfigurationDialog
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.veh_post_progression.models.progression import PostProgressionAvailability as PostProgressionAvailability, PostProgressionCompletion as PostProgressionCompletion
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
from PlayerEvents import g_playerEvents as g_playerEvents
from post_progression_common import ROLESLOT_FEATURE as ROLESLOT_FEATURE, SETUPS_FEATURES as SETUPS_FEATURES
from helpers import dependency as dependency
from helpers.algorithms import shortestPath as shortestPath
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider, IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.veh_skill_tree.logger import SkillTreeUILogger as SkillTreeUILogger
from gui.impl.lobby.exchange.exchange_rates_helper import calculateMaxPossibleFreeXp as calculateMaxPossibleFreeXp
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.tree_view_model import TreeViewModel as TreeViewModel, ResearchAvailability as ResearchAvailability
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.path_model import PathModel as PathModel, LineType as LineType
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.node_model import NodeModel as NodeModel, Type as Type, Status as Status
_logger: Any
_DIRECTION_TO_LINE_TYPE: dict
_AVAILABILITY_MAP: dict
_STEP_TYPE_TO_TOOLTIP: dict

class TreePresenter(SubModelPresenter, IPresenterLocationController):
    __RESEARCH_RESPONSE_DELAY = 1.0
    __exchangeRates: Any
    __itemsCache: Any
    __wallet: Any
    __vehicle: Any
    __selectedNodeIDs: Any
    __researchedNodeIDs: Any
    __lastSelectedNodeID: Any
    __researchInProgress: Any
    __uiLogger: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, vhCtx):
        ...
    def finalize(self):
        ...
    def clear(self):
        ...
    def _initializeLocation(self):
        ...
    def _finalizeLocation(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __onXPStatsChanged(self, *args):
        ...
    # decorador original: @adisp_process
    def __onResearch(self):
        ...
    # decorador original: @adisp_process
    # decorador original: @args2params(...)
    def __onShowNodeConfigurationWindow(self, nodeID):
        ...
    @staticmethod
    def __onFinalNodeResearchAnimationFinished():
        ...
    # decorador original: @args2params(...)
    def __onSelectNode(self, targetNodeID):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __showTreeNodeDialog(self, feature, nodeID, callback):
        ...
    def __onCacheResync(self, _, diff):
        ...
    def __onDisconnected(self):
        ...
    def __update(self):
        ...
    def __fillIntsArray(self, array):
        ...
    def __fillNodes(self, viewModel):
        ...
    def __fillNode(self, step, nodeVM):
        ...
    def __fillPath(self, step, pathVM):
        ...
    def __setVehSkillTreeHintShownFlag(self, nodeID):
        ...
    def __isHintRequired(self, step):
        ...
    def __generatePath(self, targetStep):
        ...
    def __getNodeStatus(self, step):
        ...
    def __notEnoughXp(self):
        ...
    def __onWalletStatusChanged(self, *_):
        ...
    def __getResearchState(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @wg_async
    def __showAlternateConfigurationDialog(self, feature, nodeID, callback):
        ...
    def __isPorgressionCompleted(self):
        ...
    def __isPrestigeGlareShown(self):
        ...
    def __isTreeLocked(self):
        ...
    def __updateResearchAvailability(self):
        ...
