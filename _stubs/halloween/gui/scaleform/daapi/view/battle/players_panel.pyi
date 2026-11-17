# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/players_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.shared.badges import buildBadge as buildBadge
from gui.battle_control import avatar_getter as avatar_getter
from halloween.gui.battle_control.controllers.battle_gui_controller import EventBattleGoal as EventBattleGoal
from halloween.gui.scaleform.daapi.view.meta.HWPlayersPanelMeta import HWPlayersPanelMeta as HWPlayersPanelMeta
from HWTeamInfoStatsComponent import HWTeamInfoStatsComponent as HWTeamInfoStatsComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
BattleGoalMapping: dict

class HWPlayersPanel(HWPlayersPanelMeta):
    _UPDATE_PERIOD = 0.2
    _callbackDelayer: Any
    __isPostmortem: Any
    __vehsCache: Any
    def __init__(self):
        ...
    @property
    def arenaPhases(self):
        ...
    @property
    def teamInfoStats(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _handleShowExtendedInfo(self, event):
        ...
    def __onAvatarReady(self):
        ...
    def __updateAllTeamates(self):
        ...
    def __updateTeamPanel(self):
        ...
    def __teamBuffsUpdated(self):
        ...
    def __updateTeamPanelImpl(self, forceUpdate=False):
        ...
    def __setVehicleHealth(self, vInfo, health, forceUpdate):
        ...
    def __getVehicleMaxHealth(self, vInfo):
        ...
    def __updateTeammate(self, vInfo, hpCurrent):
        ...
    def __onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def __onRespawnBaseMoving(self):
        ...
