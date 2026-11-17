# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/mode_selector/ls_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.AccountSettings import MODE_SELECTOR_BATTLE_PASS_SHOWN as MODE_SELECTOR_BATTLE_PASS_SHOWN, AccountSettings as AccountSettings
from frameworks.wulf import WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum as PerformanceRiskEnum
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import BattlePassState as BattlePassState
from gui.impl.lobby.mode_selector.items import resetBattlePassStateForItem as resetBattlePassStateForItem, BATTLE_PASS_SEASON_ID as BATTLE_PASS_SEASON_ID
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings
from last_stand.gui.ls_gui_constants import VIEW_ALIAS as VIEW_ALIAS, LS_INFO_PAGE_KEY as LS_INFO_PAGE_KEY
from last_stand.gui.shared.utils.performance_analyzer import PerformanceGroup as PerformanceGroup
from helpers import dependency as dependency, time_utils as time_utils
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem, getFormattedTimeLeft as getFormattedTimeLeft
from last_stand.skeletons.ls_controller import ILSController as ILSController
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel as ModeSelectorNormalCardModel
PERFORMANCE_MAP: dict

class LSSelectorItem(ModeSelectorLegacyItem):
    lsCtrl: Any
    bpController: Any
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
    def _isInfoIconVisible(self):
        ...
    def _onDisposing(self):
        ...
    def __onEventUpdate(self, *_):
        ...
    def __getEndDate(self):
        ...
    def __setBattlePassState(self, itemVM):
        ...
