# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/mode_selector/items/battle_royale_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_battle_royale_model import ModeSelectorBattleRoyaleModel as ModeSelectorBattleRoyaleModel
from battle_royale.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_battle_royale_widget_model import BattleRoyaleProgressionStatus as BattleRoyaleProgressionStatus
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import createAndLoadBackportTooltipWindow as createAndLoadBackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes as ModeSelectorCardTypes
from gui.impl.lobby.mode_selector.items import setBattlePassState as setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.shared.formatters import time_formatters as time_formatters
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleModeSelectorItem(ModeSelectorLegacyItem):
    _VIEW_MODEL = ModeSelectorBattleRoyaleModel
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.BATTLE_ROYALE
    __battleRoyaleController: Any
    __brProgression: Any
    @property
    def viewModel(self):
        ...
    @property
    def hasExtendedCalendarTooltip(self):
        ...
    def getExtendedCalendarTooltip(self, parentWindow):
        ...
    def handleInfoPageClick(self):
        ...
    def _onInitializing(self):
        ...
    def _isNewLabelVisible(self):
        ...
    def _onDisposing(self):
        ...
    def _getIsDisabled(self):
        ...
    def _isInfoIconVisible(self):
        ...
    def _setModeDescription(self, modeStrings):
        ...
    def __onTimerTick(self):
        ...
    def __onUpdate(self, *_):
        ...
    def __fillViewModel(self):
        ...
    @staticmethod
    def __resetViewModel(vm):
        ...
    def __fillWidgetData(self):
        ...
