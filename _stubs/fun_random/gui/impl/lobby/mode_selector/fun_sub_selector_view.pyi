# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/mode_selector/fun_sub_selector_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from battle_modifiers_ext.constants_ext import ClientDomain as ClientDomain
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, ViewStatus as ViewStatus
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState
from fun_random.gui.feature.models.common import FunSubModesStatus as FunSubModesStatus
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression, hasMultipleSubModes as hasMultipleSubModes, avoidSubModesStates as avoidSubModesStates
from fun_random.gui.impl.gen.view_models.views.lobby.feature.mode_selector.fun_random_sub_selector_card_model import FunRandomSubSelectorCardModel as FunRandomSubSelectorCardModel, CardState as CardState
from fun_random.gui.impl.gen.view_models.views.lobby.feature.mode_selector.fun_random_sub_selector_model import FunRandomSubSelectorModel as FunRandomSubSelectorModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import getFormattedTimeLeft as getFormattedTimeLeft, getConditionText as getConditionText, packProgressionConditions as packProgressionConditions, packInfiniteProgressionState as packInfiniteProgressionState, packInfiniteProgressionStage as packInfiniteProgressionStage, packInfiniteProgressionConditions as packInfiniteProgressionConditions
from fun_random.gui.impl.lobby.common.fun_view_helpers import packAdditionalRewards as packAdditionalRewards, packProgressionActiveStage as packProgressionActiveStage, packProgressionState as packProgressionState, defineProgressionStatus as defineProgressionStatus
from fun_random.gui.impl.lobby.tooltips.fun_random_domain_tooltip_view import FunRandomDomainTooltipView as FunRandomDomainTooltipView
from fun_random.gui.impl.lobby.tooltips.fun_random_loot_box_tooltip_view import FunRandomLootBoxTooltipView as FunRandomLootBoxTooltipView
from fun_random.gui.impl.lobby.tooltips.fun_random_progression_tooltip_view import FunRandomProgressionTooltipView as FunRandomProgressionTooltipView
from fun_random.gui.impl.lobby.tooltips.fun_random_reward_box_tooltip_views import NearestAdditionalRewardsTooltip as NearestAdditionalRewardsTooltip
from fun_random.gui.impl.lobby.common.fun_view_helpers import packPerformanceAlertInfo as packPerformanceAlertInfo
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID, DEFAULT_ASSETS_PACK as DEFAULT_ASSETS_PACK
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.simple_tooltip import createSimpleIconTooltip as createSimpleIconTooltip
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants as ModeSelectorTooltipsConstants
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.events import ModeSubSelectorEvent as ModeSubSelectorEvent
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, time_utils as time_utils
from shared_utils import findFirst as findFirst
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from frameworks.wulf import View as View, Array as Array
from frameworks.wulf.view.view_event import ViewEvent as ViewEvent
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode
_SUB_MODE_CARD_STATE_MAP: dict

class FunModeSubSelectorView(ViewImpl, FunAssetPacksMixin, FunSubModesWatcher, FunProgressionWatcher):
    __slots__: tuple
    __lobbyContext: Any
    __tooltips: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def abortSelection(self):
        ...
    def setDisabledProgression(self, model=None):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __getSubModeByEvent(self, event):
        ...
    def __getSubModeStartDelta(self, status):
        ...
    def __getSubModeEndDelta(self, status):
        ...
    def __createCardModel(self, subMode, selectedSubModeID):
        ...
    # decorador original: @adisp_process
    def __onSelectSubMode(self, args):
        ...
    def __onShowSubInfoPage(self, args):
        ...
    def __invalidate(self, status):
        ...
    # decorador original: @hasMultipleSubModes(...)
    # decorador original: @avoidSubModesStates(...)
    def __invalidateAll(self, status, *_):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateProgression(self, *_):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateProgressionTimer(self, *_):
        ...
    # decorador original: @hasMultipleSubModes(...)
    def __invalidateSubModesCards(self, cards):
        ...
    def __invalidateSubModesTimer(self, *_):
        ...
    # decorador original: @hasActiveProgression(...)
    def __fillProgression(self, model):
        ...
    def __toggleSelectorClickProcessing(self, isClickProcessing):
        ...
