# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/mode_selector/fort_rush_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fort_rush.gui.fort_rush_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from fort_rush.gui.game_control.perfomance_analyzer_controller import PerformanceGroup as PerformanceGroup
from fort_rush.gui.impl.gen.view_models.views.lobby.mode_selector.fort_rush_mode_selector_model import FortRushModeSelectorModel as FortRushModeSelectorModel
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from fort_rush.gui.shared.event_dispatcher import showFortRushInfoPage as showFortRushInfoPage
from gui.shared.utils import SelectorBattleTypesUtils as SelectorBattleTypesUtils
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum as PerformanceRiskEnum
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from fort_rush.gui.impl.gen.view_models.views.lobby.mode_selector.fort_rush_mode_selector_model import FortRushModeSelectorWidgetModel as FortRushModeSelectorWidgetModel
PERFORMANCE_MAP: dict

class FortRushModeSelectorItem(ModeSelectorLegacyItem):
    __frCtrl: Any
    __itemsCache: Any
    _VIEW_MODEL = FortRushModeSelectorModel
    @property
    def viewModel(self):
        ...
    @property
    def isSelectable(self):
        ...
    @property
    def isVisible(self):
        ...
    def _getPositionByModeName(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def _fillProgressionWidget(self, vm):
        ...
    def __onCacheSyncCompleted(self, reason, diff):
        ...
    def _isInfoIconVisible(self):
        ...
    def handleInfoPageClick(self):
        ...
