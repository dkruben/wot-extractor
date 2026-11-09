# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PoiTeamInfoComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from script_component.ScriptComponent import ScriptComponent as ScriptComponent
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.arena_info.interfaces import IPointsOfInterestController as IPointsOfInterestController
_logger: Any

class PoiTeamInfoComponent(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.POINTS_OF_INTEREST
    __sessionProvider: Any
    def __init__(self):
        ...
    def onEnterWorld(self, _):
        ...
    def onLeaveWorld(self):
        ...
    def onPoiEquipmentUsed(self, vehicleID, equipmentID):
        ...
    def onPoiCaptured(self, poiID, vehicleID):
        ...
    def onPoiInvaderDestroyed(self, vehicleID):
        ...
