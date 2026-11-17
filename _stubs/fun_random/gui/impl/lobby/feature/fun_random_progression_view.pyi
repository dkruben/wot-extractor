# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/fun_random_progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import BigWorld as BigWorld
import math_utils as math_utils
from account_helpers.AccountSettings import AccountSettings as AccountSettings, FUN_RANDOM_PROGRESSION_OPENED as FUN_RANDOM_PROGRESSION_OPENED, FUN_RANDOM_PROGRESSION as FUN_RANDOM_PROGRESSION, FUN_RANDOM_PROGR_PREV_COUNTER as FUN_RANDOM_PROGR_PREV_COUNTER, FUN_RANDOM_INF_PROGR_PREV_COUNTER as FUN_RANDOM_INF_PROGR_PREV_COUNTER, FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT as FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from fun_random.gui.feature.fun_sounds import FUN_PROGRESSION_SOUND_SPACE as FUN_PROGRESSION_SOUND_SPACE
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from fun_random.gui.impl.gen.view_models.views.lobby.feature.fun_random_progression_view_model import FunRandomProgressionViewModel as FunRandomProgressionViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import packAdditionalRewards as packAdditionalRewards, packFullProgressionConditions as packFullProgressionConditions, packProgressionStages as packProgressionStages, packProgressionState as packProgressionState, packInfiniteProgressionStage as packInfiniteProgressionStage, packFullInfiniteProgressionConditions as packFullInfiniteProgressionConditions
from fun_random.gui.impl.lobby.tooltips.fun_random_loot_box_tooltip_view import FunRandomLootBoxTooltipView as FunRandomLootBoxTooltipView
from fun_random.gui.shared.event_dispatcher import showFunRandomTierList as showFunRandomTierList
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared.event_dispatcher import showHangar as showHangar
_DESTROY_ACTION_NAME = 'showHangar'

class FunRandomProgressionView(ViewImpl, FunAssetPacksMixin, FunProgressionWatcher, FunSubModesWatcher):
    __slots__: tuple
    _COMMON_SOUND_SPACE = FUN_PROGRESSION_SOUND_SPACE
    __tooltips: Any
    __saveProgressCallbackId: Any
    def __init__(self, *_, **__):
        ...
    @staticmethod
    def showHangar(*_):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _showTierList(self, *_):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidate(self):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateAll(self, *_):
        ...
    # decorador original: @hasActiveProgression(...)
    def __invalidateTimer(self, *_):
        ...
    def __saveProgress(self):
        ...

class FunRandomProgressionWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
