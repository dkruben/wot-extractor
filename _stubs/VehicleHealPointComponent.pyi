# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleHealPointComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from helpers import dependency as dependency
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from Event import EventsSubscriber as EventsSubscriber
HealPointInfo: Any

class VehicleHealPointComponent(BigWorld.DynamicScriptComponent):
    __dynamicObjectsCache: Any
    __EQUIPMENT_NAME = BattleRoyaleEquipments.HEAL_POINT
    __es: Any
    def __init__(self, *args):
        ...
    def set_endTime(self, prev):
        ...
    def onDestroy(self):
        ...
    def onLeaveWorld(self, *args):
        ...
    def __onUpdated(self, info=None):
        ...
    def __getEffectSettings(self):
        ...
    def __onUpdateObservedVehicleData(self, vehicleID, *args):
        ...
    def __onVehicleUpgradeFinished(self, vehicleID):
        ...
