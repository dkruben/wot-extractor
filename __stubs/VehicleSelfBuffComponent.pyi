# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleSelfBuffComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as BATTLE_MARKER_STATES
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent as VehicleAbilityBaseComponent

class VehicleSelfBuffComponent(VehicleAbilityBaseComponent):
    EQUIPMENT_NAME = BattleRoyaleEquipments.SELF_BUFF
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.INSPIRE
    __MARKER_ID = BATTLE_MARKER_STATES.INSPIRING_STATE
    def __init__(self):
        ...
    def _updateTimer(self, data):
        ...
    def _getDuration(self):
        ...
