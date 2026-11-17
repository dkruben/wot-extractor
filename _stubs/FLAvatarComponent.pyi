# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/FLAvatarComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
from ReservesEvents import randomReservesEvents as randomReservesEvents
from frontline_common.constants import CallbackDataNames as CallbackDataNames
from frontline.FLReplayController import FLReplayController as FLReplayController
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent

class FLAvatarComponent(DynamicScriptComponent):
    __guiSessionProvider: Any
    def onDestroy(self):
        ...
    def _onAvatarReady(self):
        ...
    def callCtrl(self, func, *args):
        ...
    def updateRespawnVehicles(self, vehsList):
        ...
    def updateRespawnCooldowns(self, cooldowns):
        ...
    def updateRespawnInfo(self, respawnInfo):
        ...
    def updateVehicleLimits(self, respawnLimits):
        ...
    def onTeamLivesRestored(self, teams):
        ...
    def updatePlayerLives(self, lives):
        ...
