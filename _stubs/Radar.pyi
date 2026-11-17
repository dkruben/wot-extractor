# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/Radar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
from Math import Vector3 as Vector3
import BattleReplay as BattleReplay
from helpers import dependency as dependency
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class Radar(BigWorld.DynamicScriptComponent):
    __dynObjectsCache: Any
    __sessionProvider: Any
    def onEnterWorld(self, *args):
        ...
    def onLeaveWorld(self, *args):
        ...
    def set_radarReadinessTime(self, _=None):
        ...
    def set_radarReady(self, prev=None):
        ...
    def refreshRadar(self):
        ...
    def activatePatrickEffect(self):
        ...
    def __playEffect(self):
        ...
