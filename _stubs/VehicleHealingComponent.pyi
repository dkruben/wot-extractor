# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleHealingComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent as VehicleAbilityBaseComponent
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments

class VehicleHealingComponent(VehicleAbilityBaseComponent):
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.HEALING
    __MARKER_ID = BATTLE_MARKER_STATES.HEALING_STATE
    _isDestroying: Any
    def __init__(self):
        ...
    def set_isInactivation(self, prev):
        ...
    def _updateTimer(self, data):
        ...
    def _updateMarker(self, data, isHide=False):
        ...
    def _destroy(self):
        ...
    def _getDuration(self):
        ...
    def _getHealingArgs(self):
        ...
