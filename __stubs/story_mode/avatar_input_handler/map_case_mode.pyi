# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/avatar_input_handler/map_case_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import BigWorld as BigWorld
from typing import Optional as Optional, Any as Any
from story_mode.cgf_components.bunkers import BunkersSystem as BunkersSystem
from BunkerLogicComponent import BunkerLogicComponent as BunkerLogicComponent
import CGF as CGF
from AvatarInputHandler import MapCaseMode as MapCaseMode
from Math import Vector3 as Vector3
from story_mode_common.story_mode_constants import VEHICLE_BUNKER_TURRET_TAG as VEHICLE_BUNKER_TURRET_TAG
POSITION_PRECISION = 0.001

class StrikeSelector(MapCaseMode._ArcadeBomberStrikeSelector):
    _edgedBunkers: _Any
    def __init__(self, position, equipment):
        ...
    def destroy(self):
        ...
    def highlightVehicles(self):
        ...
    def _validateVehicle(self, vehicle):
        ...
    def _clearEdgedDestructibles(self):
        ...
    @staticmethod
    def _getBunkerComponent(destructibleEntityID):
        ...

class NavMeshCheckingSelector(MapCaseMode._ArenaBoundsAreaStrikeSelector):
    _CHECK_SERVER_DELAY = 0.1
    _updateTimerID: _Any
    _checkPosition: _Any
    _prevCheckPosition: _Any
    def __init__(self, position, equipment, direction=...):
        ...
    def processHover(self, position, force=False):
        ...
    def processSelection(self, position, reset=False):
        ...
    def destroy(self):
        ...
    @property
    def _avatarComponent(self):
        ...
    def _validatePosition(self, position):
        ...
    def _updateFromServer(self):
        ...
    def _onPositionValidChanged(self):
        ...

class ReconAbilitySelector(NavMeshCheckingSelector):
    ...

class DistractionAbilitySelector(NavMeshCheckingSelector):
    ...

def _vectorEqual(first, second):
    ...
