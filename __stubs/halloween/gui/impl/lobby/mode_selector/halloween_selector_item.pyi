# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/mode_selector/halloween_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.AccountSettings import MODE_SELECTOR_BATTLE_PASS_SHOWN as MODE_SELECTOR_BATTLE_PASS_SHOWN, AccountSettings as AccountSettings
from helpers.time_utils import ONE_DAY as ONE_DAY
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum as PerformanceRiskEnum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import BattlePassState as BattlePassState
from gui.impl.lobby.mode_selector.items import resetBattlePassStateForItem as resetBattlePassStateForItem, BATTLE_PASS_SEASON_ID as BATTLE_PASS_SEASON_ID
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem, getFormattedTimeLeft as getFormattedTimeLeft
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings
from halloween.gui.shared.event_dispatcher import showInfoPage as showInfoPage
from halloween.gui.shared.utils.performance_analyzer import PerformanceGroup as PerformanceGroup
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from helpers import dependency as dependency, time_utils as time_utils, int2roman as int2roman
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel as ModeSelectorNormalCardModel
PERFORMANCE_MAP: dict

class HalloweenSelectorItem(ModeSelectorLegacyItem):
    __hwBattleCtrl: Any
    __hwArtefactsCtrl: Any
    __bpController: Any
    __uiLogger: Any
    def _onInitializing(self):
        ...
    @property
    def isSelectable(self):
        ...
    @property
    def calendarTooltipText(self):
        ...
    def handleClick(self):
        ...
    def handleInfoPageClick(self):
        ...
    def _onDisposing(self):
        ...
    def _isInfoIconVisible(self):
        ...
    def __onHalloweenUpdate(self, *_):
        ...
    def __getEndDate(self):
        ...
    def __setBattlePassState(self, itemVM):
        ...
