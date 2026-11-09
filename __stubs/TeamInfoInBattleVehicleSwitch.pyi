# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TeamInfoInBattleVehicleSwitch.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import VehicleSelectionPlayerStatus as VehicleSelectionPlayerStatus
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from script_component.ScriptComponent import ScriptComponent as ScriptComponent

class TeamInfoInBattleVehicleSwitch(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION
    __sessionProvider: Any
    __positionsSet: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_positions(self, _):
        ...
    def set_statuses(self, prevValues):
        ...
    def checkVehicleConfirmation(self, vehicleID):
        ...
    def __setPositions(self):
        ...
    def __updateStatuses(self, statuses):
        ...
    @staticmethod
    def __getNewValues(prevValues, newValues):
        ...
