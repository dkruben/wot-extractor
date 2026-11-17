# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import KillCamMarkersManager as KillCamMarkersManager
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage as ClassicPage
from gui.Scaleform.daapi.view.battle.shared import drone_music_player as drone_music_player, finish_sound_player as finish_sound_player
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer as CrosshairPanelContainer
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer as StartCountdownSoundPlayer
from gui.Scaleform.daapi.view.battle.maps_training import markers2d as markers2d, arena_time_notificator as arena_time_notificator
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
MAPS_TRAINING_CONFIG: Any
_MAPS_TRAINING_EXTERNAL_COMPONENTS: tuple

class DynamicAliases(CONST_CONTAINER):
    PREBATTLE_TIMER_SOUND_PLAYER = 'prebattleTimerSoundPlayer'
    FINISH_SOUND_PLAYER = 'finishSoundPlayer'
    DRONE_MUSIC_PLAYER = 'droneMusicPlayer'
    TIME_NOTIFIER = 'arenaTimeNotificator'

class MapsTrainingPage(ClassicPage):
    def __init__(self, components=..., external=..., fullStatsAlias=None, **kwargs):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
