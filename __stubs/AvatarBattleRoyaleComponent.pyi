# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/AvatarBattleRoyaleComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
import BattleReplay as BattleReplay
from BattleReplay import g_replayEvents as g_replayEvents
from Event import EventsSubscriber as EventsSubscriber

class AvatarBattleRoyaleComponent(BigWorld.DynamicScriptComponent, EventsSubscriber):
    sessionProvider: Any
    def __init__(self):
        ...
    def onLeaveWorld(self):
        ...
    def set_playerPlace(self, _prev):
        ...
    def __onTimeWarpStart(self):
        ...
    def __onTimeWarpFinish(self):
        ...
