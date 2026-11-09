# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/battle_quests_done_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import setSeasonInfo as setSeasonInfo
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as Comp7LightSeasonState
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName as Comp7LightSeasonName
from comp7_light.gui.impl.gen.view_models.views.lobby.tooltips.battle_quests_done_tooltip_model import BattleQuestsDoneTooltipModel as BattleQuestsDoneTooltipModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class BattleQuestsDoneTooltip(ViewImpl):
    __comp7LightController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onStatusUpdated(self, _):
        ...
    def _onStatusTick(self):
        ...
    def _updateState(self):
        ...
    def __onPollServerTime(self):
        ...
