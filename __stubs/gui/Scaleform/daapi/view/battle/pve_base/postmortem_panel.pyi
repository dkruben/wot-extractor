# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/postmortem_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import WWISE as WWISE
from TeamInfoLivesComponent import TeamInfoLivesComponent as TeamInfoLivesComponent
from gui.Scaleform.daapi.view.meta.PvePostmortemPanelMeta import PvePostmortemPanelMeta as PvePostmortemPanelMeta
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.respawn_hud import RespawnHUDClientModel as RespawnHUDClientModel
from math_common import round_py2_style as round_py2_style
from pve_battle_hud import WidgetType as WidgetType
_TIMER_ZERO_VALUE = '00:00'

class LivesState(IntEnum):
    NONE = 1
    HAS_LIVES = 2
    HAS_LOCKED_LIVES = 3
    NO_LIVES = 4

class PvePostmortemPanel(PvePostmortemPanelMeta):
    __slots__: tuple
    _RESPAWN_TIMER_SOUND_EVENT = 'sm_gp_vday_respawn_start'
    _settings: Any
    _livesState: Any
    def __init__(self):
        ...
    def resetDeathInfo(self):
        ...
    def updateTime(self, value):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def _onBattleSessionStop(self):
        ...
    def _settingsChangeHandler(self, settingsID):
        ...
    @property
    def _respawnComponent(self):
        ...
    @property
    def _teamLives(self):
        ...
    def _onTeamLivesUpdated(self):
        ...
    def _showOwnDeathInfo(self):
        ...
    def _updateLivesState(self):
        ...
    def _calcCurrentLivesState(self):
        ...
    def _applyLivesState(self, livesState):
        ...
    @property
    def _currentRespawnDelay(self):
        ...
    @staticmethod
    def _playSound(name):
        ...
