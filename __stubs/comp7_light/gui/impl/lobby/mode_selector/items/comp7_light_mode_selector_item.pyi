# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/mode_selector/items/comp7_light_mode_selector_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_comp7_light_model import ModeSelectorComp7LightModel as ModeSelectorComp7LightModel
from comp7_light.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_comp7_light_widget_model import Comp7LightProgressionStatus as Comp7LightProgressionStatus
from comp7_light.skeletons.gui.game_control import IComp7LightProgressionController as IComp7LightProgressionController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem as ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID as ModeSelectorRewardID
from gui.impl.lobby.mode_selector.items import setBattlePassState as setBattlePassState
from gui.shared.formatters import time_formatters as time_formatters
from helpers import dependency as dependency, time_utils as time_utils, int2roman as int2roman
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightModeSelectorItem(ModeSelectorLegacyItem):
    __comp7LightController: Any
    __comp7LightProgressionController: Any
    _VIEW_MODEL = ModeSelectorComp7LightModel
    @property
    def viewModel(self):
        ...
    def _onInitializing(self):
        ...
    def _onDisposing(self):
        ...
    def __onDataChange(self):
        ...
    def __updateComp7LightData(self):
        ...
    def __getCurrentSeasonTimeLeft(self, currentSeason):
        ...
    def __fillModeData(self):
        ...
    def __fillWidgetData(self):
        ...
