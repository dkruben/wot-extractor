# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/vehicle_health_broadcast_listener_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class VehicleHealthBroadcastListenerComponent(object):
    guiSessionProvider: Any
    def onEnterWorld(self, prereqs=None):
        ...
    def onLeaveWorld(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomePlayer(self):
        ...
    def onBecomeNonPlayer(self):
        ...
    def onVehicleHealthChanged(self, vehicleID, newHealth, attackerID, attackReasonID, attackReasonExtID):
        ...
