# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/avatar_input_handler/map_case_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from Math import Vector2 as Vector2
from AvatarInputHandler.MapCaseMode import _ArenaBoundArtilleryStrikeSelector as _ArenaBoundArtilleryStrikeSelector, _DEFAULT_STRIKE_DIRECTION as _DEFAULT_STRIKE_DIRECTION
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class Comp7ArenaBoundArtilleryStrikeSelector(_ArenaBoundArtilleryStrikeSelector):
    __sessionProvider: Any
    def __init__(self, position, equipment, direction=...):
        ...
    def destroy(self):
        ...
    def _getAreaSize(self):
        ...
    def _getRadius(self):
        ...
    def __onRoleEquipmentStateChanged(self, state, previousState=None):
        ...

class Comp7ArenaBoundPlaneStrikeSelector(Comp7ArenaBoundArtilleryStrikeSelector):
    def __init__(self, position, equipment):
        ...

class Comp7PoiArtilleryStrikeSelector(_ArenaBoundArtilleryStrikeSelector):
    def _getAreaSize(self):
        ...
    def _getRadius(self):
        ...

class Comp7PoiIlluminationFlareStrikeSelector(_ArenaBoundArtilleryStrikeSelector):
    def _getAreaSize(self):
        ...
    def _getRadius(self):
        ...
