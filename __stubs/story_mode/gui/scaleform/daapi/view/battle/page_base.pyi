# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/page_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from logging import getLogger as getLogger
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer as CrosshairPanelContainer
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.event_dispatcher import toggleCrosshairVisibility as toggleCrosshairVisibility
from story_mode.gui.impl.battle.prebattle_window import getOpenedPrebattleView as getOpenedPrebattleView
from story_mode.gui.scaleform.daapi.view.battle.markers2d import StoryModeMarkersManager as StoryModeMarkersManager
from story_mode.gui.scaleform.genConsts.STORY_MODE_BATTLE_VIEW_ALIASES import STORY_MODE_BATTLE_VIEW_ALIASES as STORY_MODE_BATTLE_VIEW_ALIASES
from story_mode.gui.shared.event_dispatcher import showIntro as showIntro
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME
STORY_MODE_EXTERNAL_COMPONENTS: tuple
_logger: Any

class StoryModeBattlePageBase(object):
    _isWinMessageShown: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def isWinMessageShown(self):
        ...
    def hideAndStop(self):
        ...
    def reload(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _handleGUIToggled(self, event):
        ...
    def _hasBattleMessenger(self):
        ...
    def _hasCalloutPanel(self):
        ...
    def showWinMessage(self, team, reason):
        ...
    def _onBattleLoadingStart(self):
        ...
    def __onRoundFinished(self, *_):
        ...
