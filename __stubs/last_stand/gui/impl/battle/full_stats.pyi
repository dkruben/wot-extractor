# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/battle/full_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent
from LSTeamInfoStatsComponent import LSTeamInfoStatsComponent as LSTeamInfoStatsComponent
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from last_stand.gui.impl.gen.view_models.views.battle.full_stats_view_model import FullStatsViewModel as FullStatsViewModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from last_stand_common.last_stand_constants import ARENA_BONUS_TYPE_TO_LEVEL as ARENA_BONUS_TYPE_TO_LEVEL
from helpers import dependency as dependency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from last_stand.gui.impl.lobby.widgets.event_stats import EventStats as EventStats
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class FullEventStatsView(ViewImpl):
    _sessionProvider: Any
    _FIRST_PHASE = 1
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @classmethod
    def getLayoutID(cls):
        ...
    @property
    def vehicleStats(self):
        ...
    @property
    def arenaPhases(self):
        ...
    @property
    def activePhase(self):
        ...
    @property
    def battleGUICtrl(self):
        ...
    @property
    def viewModel(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateHeader(self, model=None):
        ...
    def __onPhaseChanged(self):
        ...

class FullEventStatsWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
