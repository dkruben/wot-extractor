# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_cfg_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from Event import Event as Event
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel
from gui.impl.gen.view_models.views.lobby.post_progression.step_model import StepState as StepState
from gui.impl.gen.view_models.views.lobby.post_progression.modification_model import ModificationModel as ModificationModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import ProgressionAvailability as ProgressionAvailability, ProgressionState as ProgressionState
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_cfg_view_model import PostProgressionCfgViewModel as PostProgressionCfgViewModel
from gui.impl.lobby.veh_post_progression.post_progression_base_component import PostProgressionBaseComponentView as PostProgressionBaseComponentView
from gui.impl.lobby.veh_post_progression.tooltips.pair_modification_tooltip_view import CfgPairModificationTooltipView as CfgPairModificationTooltipView
from gui.impl.lobby.veh_post_progression.tooltips.level_tooltip_view import CfgProgressionLevelTooltipView as CfgProgressionLevelTooltipView
from gui.impl.lobby.veh_post_progression.tooltips.role_slot_tooltip_view import RoleSlotTooltipView as RoleSlotTooltipView
from gui.impl.lobby.veh_post_progression.tooltips.setup_tooltip_view import SetupTooltipView as SetupTooltipView
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.veh_post_progression.helpers import storeLastSeenStep as storeLastSeenStep
from gui.veh_post_progression.models.ext_money import ExtendedMoney as ExtendedMoney, ExtendedCurrency as ExtendedCurrency, EXT_MONEY_UNDEFINED as EXT_MONEY_UNDEFINED
from gui.veh_post_progression.models.progression import PostProgressionAvailability as PostProgressionAvailability, PostProgressionCompletion as PostProgressionCompletion
from gui.veh_post_progression.models.progression_step import PostProgressionStepState as PostProgressionStepState
from gui.veh_post_progression.models.purchase import PurchaseCheckResult as PurchaseCheckResult, PurchaseProvider as PurchaseProvider
from helpers import dependency as dependency
from items import vehicles as vehicles
from post_progression_common import GROUP_ID_BY_FEATURE as GROUP_ID_BY_FEATURE, ACTION_TYPES as ACTION_TYPES
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import IWalletController as IWalletController
from gui.impl.gen.view_models.common.price_model import PriceModel as PriceModel
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel as BonusesModel
from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel as MultiStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel as SingleStepModel
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
_AVAILABILITY_MAP: dict
_COMPLETION_MAP: dict
_STEP_STATE_MAP: dict
_TOGGLING_COOLDOWN = 1.0

class PostProgressionCfgComponentView(PostProgressionBaseComponentView):
    __itemsCache: Any
    __walletController: Any
    __slots__: tuple
    __balance: Any
    __intCD: Any
    onGoBackAction: Any
    onResearchAction: Any
    __togglingSteps: Any
    __lockTogglingCallbackID: Any
    __creditsRate: Any
    _vehicle: Any
    def __init__(self, layoutID=..., **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def invalidateVehicle(self, intCD):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, intCD=None, **kwargs):
        ...
    def _updateAll(self, *_):
        ...
    def __updateLastSeenModification(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    # decorador original: @adisp_process
    def _onMainStepActionClick(self, args):
        ...
    # decorador original: @adisp_process
    def _onPrebattleSwitchToggleClick(self, args):
        ...
    # decorador original: @adisp_process
    def _onMultiStepActionClick(self, args):
        ...
    def _updateVehicle(self, **kwargs):
        ...
    def _updateViewModel(self, viewModel, availabilityReason, completion):
        ...
    def _fillControlsModel(self, model, postProgression):
        ...
    def _fillModification(self, modModel, modification):
        ...
    def _fillMultiStepModel(self, stepModel, step, selectedModID):
        ...
    def _fillPersistentBonuses(self, bonuses, postProgression, completion):
        ...
    def _fillSingleStepModel(self, stepModel, step):
        ...
    # decorador original: @adisp_process
    def __onPurchaseClick(self):
        ...
    def __onGoBackAction(self):
        ...
    def __onResearchAction(self):
        ...
    def __onSyncCompleted(self, reason, diff):
        ...
    def __lockToggling(self):
        ...
    def __unlockToggling(self):
        ...
    def __cancelLockToggling(self):
        ...
    def __updateTogglingLock(self, isLocked):
        ...
    def __fillPriceModel(self, priceModel, price, checkResult):
        ...
    def __getStepsToPurchase(self, postProgression):
        ...
    def __getUnlockedMainSteps(self, postProgression):
        ...
    def __updateMoney(self, *_):
        ...
