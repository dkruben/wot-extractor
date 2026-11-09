# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/mode_selector/items/fun_random_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import math_utils as math_utils
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression, hasAnySubMode as hasAnySubMode, hasMultipleSubModes as hasMultipleSubModes, avoidSubModesStates as avoidSubModesStates
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionStatus as FunRandomProgressionStatus
from fun_random.gui.impl.lobby.common.fun_view_helpers import defineProgressionStatus as defineProgressionStatus
from fun_random.gui.impl.lobby.common.fun_view_helpers import getFormattedTimeLeft as getFormattedTimeLeft
from fun_random.gui.impl.lobby.mode_selector.items.fun_random_mode_selector_helpers import createSelectorHelper as createSelectorHelper
from fun_random.gui.impl.lobby.common.fun_view_helpers import packPerformanceAlertInfo as packPerformanceAlertInfo
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes as ModeSelectorCardTypes
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_fun_random_model import ModeSelectorFunRandomModel as ModeSelectorFunRandomModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_fun_random_widget_model import SimpleFunProgressionStatus as SimpleFunProgressionStatus
from gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants as ModeSelectorTooltipsConstants
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.server_events.bonuses import LootBoxTokensBonus as LootBoxTokensBonus
from helpers import time_utils as time_utils
from frameworks.wulf import Array as Array
from fun_random.gui.feature.models.common import FunSubModesStatus as FunSubModesStatus
from fun_random.gui.impl.lobby.mode_selector.items.fun_random_mode_selector_helpers import IModeSelectorHelper as IModeSelectorHelper
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_fun_random_widget_model import ModeSelectorFunRandomWidgetModel as ModeSelectorFunRandomWidgetModel
_PROGRESSION_STATUS_MAP: dict

class FunRandomSelectorItem(ModeSelectorLegacyItem, FunAssetPacksMixin, FunSubModesWatcher, FunProgressionWatcher):
    __slots__: tuple
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.FUN_RANDOM
    _VIEW_MODEL = ModeSelectorFunRandomModel
    __subModesHelper: Any
    def __init__(self, oldSelectorItem):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @hasMultipleSubModes(...)
    def checkHeaderNavigation(self):
        ...
    def setDisabledProgression(self):
        ...
    def handleInfoPageClick(self):
        ...
    # decorador original: @hasMultipleSubModes(...)
    def _isInfoIconVisible(self):
        ...
    def _isNewLabelVisible(self):
        ...
    def _getModeStringsRoot(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def __getStatusText(self, status):
        ...
    def __getTimeLeftText(self, status):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    # decorador original: @avoidSubModesStates(...)
    def __invalidateAll(self, status, *_):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateProgression(self, *_):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateProgressionTimer(self, *_):
        ...
    # decorador original: @hasAnySubMode(...)
    def __invalidateSubModesTimer(self, *_):
        ...
    def __invalidateNewLabel(self, *_):
        ...
    def __invalidateRewards(self, rewards):
        ...
    # decorador original: @hasAnySubMode(...)
    def __fillCardModel(self, model, status):
        ...
    # decorador original: @hasActiveProgression(...)
    def __fillProgression(self, model):
        ...
    # decorador original: @hasActiveProgression(...)
    def __fillProgressionReward(self):
        ...
    def __reloadModeHelper(self):
        ...
