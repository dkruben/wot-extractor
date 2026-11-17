# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/players_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from last_stand.gui.scaleform.daapi.view.battle.voip_helper import LSVoipHelper as LSVoipHelper
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.shared.badges import buildBadge as buildBadge
from gui.battle_control import avatar_getter as avatar_getter
from last_stand.gui.scaleform.daapi.view.meta.LSPlayersPanelMeta import LSPlayersPanelMeta as LSPlayersPanelMeta
from LSTeamInfoStatsComponent import LSTeamInfoStatsComponent as LSTeamInfoStatsComponent
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent

class LSPlayersPanel(LSPlayersPanelMeta):
    _UPDATE_PERIOD = 0.2
    _callbackDelayer: Any
    __isPostmortem: Any
    __vehsCache: Any
    __voipHelper: Any
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
    def onVoiceChatClick(self):
        ...
    def onTalkDown(self):
        ...
    def onTalkUp(self):
        ...
    def _dispose(self):
        ...
    def __onAvatarReady(self):
        ...
    def __updateAllTeamates(self):
        ...
    def __updateTeamPanel(self):
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
