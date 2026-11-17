# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInBattleVehicleSwitch.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from helpers import dependency as dependency
from script_component.ScriptComponent import ScriptComponent as ScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class AvatarInBattleVehicleSwitch(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION
    __sessionProvider: Any
    def set_vehicleSpawnList(self, _):
        ...
    def set_spawnInfoForVehicle(self, _):
        ...
    def confirmSelection(self):
        ...
    def chooseVehicle(self, newCD):
        ...
    def switchSetup(self, vehTypeCD, groupId, layoutIdx):
        ...
    def _onAvatarReady(self):
        ...
    def __updateAllVehsList(self):
        ...
    def __updateCurrentVehicle(self):
        ...
