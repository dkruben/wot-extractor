# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/script_component/ScriptComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import Avatar as Avatar
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from shared_utils import nextTick as nextTick
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class ScriptComponent(BigWorld.StaticScriptComponent):
    __sessionProvider: Any
    REQUIRED_BONUS_CAP = None
    def __init__(self):
        ...
    @property
    def _isAvatarReady(self):
        ...
    def onEnterWorld(self, _):
        ...
    def onLeaveWorld(self):
        ...
    def _onAvatarReady(self):
        ...
    def __onAvatarReady(self):
        ...
    def __checkBonusCaps(self):
        ...
