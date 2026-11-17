# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/SpawnKeyPointTeamInfo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from shared_utils import nextTick as nextTick
from AvatarInputHandler.control_modes import ArcadeControlMode as ArcadeControlMode
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from battle_royale_client_common.SpawnKeyPointTeamInfoBase import SpawnKeyPointTeamInfoBase as SpawnKeyPointTeamInfoBase

class SpawnKeyPointTeamInfo(SpawnKeyPointTeamInfoBase, DynamicScriptComponent):
    guiSessionProvider: Any
    onReceiveTeamSpawnKeyPoints: Any
    onCloseChooseSpawnKeyPointsWindow: Any
    def _onAvatarReady(self):
        ...
    def set_spawnKeyPointsCloseTime(self, prev):
        ...
    def onDestroy(self):
        ...
    def __onReceiveTeamSpawnKeyPoints(self, points):
        ...
    def __onCloseChooseSpawnKeyPointsWindow(self):
        ...
    def _avatar(self):
        ...
