# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/postmortem_panel/postmortem_panel_view.py (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, PlayerSatisfactionRating as PlayerSatisfactionRating
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.postmorten_panel.postmortem_info_panel_view_model import PostmortemInfoPanelViewModel as PostmortemInfoPanelViewModel
from gui.impl.gen.view_models.views.battle.postmorten_panel.rating_button_model import RateButtonEnum as RateButtonEnum
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.events import DeathCamEvent as DeathCamEvent
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl.common.player_satisfaction_rating.player_satisfaction_sound import playSoundForRating as playSoundForRating
from player_satisfaction_schema import playerSatisfactionSchema as playerSatisfactionSchema
from typing import Tuple as Tuple, Optional as Optional, Callable as Callable
from Event import Event as Event
from constants import FINISH_REASON as FINISH_REASON
absolute_import: Any
BONUS_TYPE: Any
_logger: Any
_MODEL_TO_COMMON_ENUM_MAP: Any
SELECTION_ORDER: Any
_COMMON_TO_MODEL_ENUM_MAP: Any

# gerado do bytecode: classes base desconhecidas
class PostmortemPanelView:
    sessionProvider: Any
    _PostmortemPanelView__BLINK_DURATION: Any
    _PostmortemPanelView__onPostMortemSwitched: Any
    _PostmortemPanelView__onKillCamStateChanged: Any
    _PostmortemPanelView__startHint: Any
    _PostmortemPanelView__stopHint: Any
    _PostmortemPanelView__onRateButtonClick: Any
    def __init__(self):
        ...
    def viewModel(self):
        ...
    def isRatingWidgetEnabled(self):
        ...
    def _getEvents(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onPostMortemSwitched(self, *_):
        ...
    def __onKillCamStateChanged(self, state, _):
        ...
    def __startHint(self):
        ...
    def __stopHint(self):
        ...
    def __onRateButtonClick(self, rating):
        ...
    def _onRoundFinished(self, winnerTeam, reason):
        ...
    def _setButtonConfig(self, model):
        ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
