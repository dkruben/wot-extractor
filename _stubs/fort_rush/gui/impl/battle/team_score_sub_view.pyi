# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/battle/team_score_sub_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_base_capture_indicator_model import FortRushBaseCaptureTeam as FortRushBaseCaptureTeam
from fort_rush.gui.shared.events import CapturePointEvent as CapturePointEvent
from fort_rush.gui.shared.team_utils import getTeamValue as getTeamValue
from fort_rush_common.component_helpers import getScoreComponent as getScoreComponent
from gui.battle_control import avatar_getter as avatar_getter
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, EventPriority as EventPriority
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class TeamScoreSubView(EventsHandler):
    __sessionProvider: Any
    __hudViewModelRef: Any
    __teamCaptures: Any
    __pointOwners: Any
    __scoreComponent: Any
    def __init__(self, hudVMRef):
        ...
    def init(self):
        ...
    def dispose(self):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    def __onTeamsScoreUpdated(self, updatedScore):
        ...
    def __onInitCapturablePoint(self, event):
        ...
    def __onCapturePointUpdate(self, event):
        ...
    def __notifyFE(self, team, count):
        ...
