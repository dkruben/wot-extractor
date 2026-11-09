# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/mode_selector/items/comp7_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers as comp7_model_helpers, comp7_shared as comp7_shared, comp7_qualification_helpers as comp7_qualification_helpers
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.lobby.tooltips.progression_tooltip import ProgressionTooltip as ProgressionTooltip
from comp7.gui.impl.lobby.tooltips.rank_inactivity_tooltip import RankInactivityTooltip as RankInactivityTooltip
from gui.impl import backport as backport
from gui.impl.gen import R as R
from comp7.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_comp7_model import ModeSelectorComp7Model as ModeSelectorComp7Model
from gui.impl.lobby.mode_selector.items import setBattlePassState as setBattlePassState
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.shared.formatters import time_formatters as time_formatters
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_comp7_widget_model import ModeSelectorComp7WidgetModel as ModeSelectorComp7WidgetModel

class Comp7ModeSelectorItem(ModeSelectorLegacyItem):
    __comp7Controller: Any
    __slots__: tuple
    _VIEW_MODEL = ModeSelectorComp7Model
    __currentSeason: Any
    def __init__(self, oldSelectorItem):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def __onDataChange(self, *_, **__):
        ...
    def __updateComp7Data(self):
        ...
    def __fillViewModel(self):
        ...
    def __getSeasonTimeLeft(self):
        ...
    def __fillWidgetData(self):
        ...
