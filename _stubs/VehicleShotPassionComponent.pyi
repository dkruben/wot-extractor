# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleShotPassionComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent as VehicleAbilityBaseComponent

class VehicleShotPassionComponent(VehicleAbilityBaseComponent):
    EQUIPMENT_NAME = BattleRoyaleEquipments.SHOT_PASSION
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.SHOT_PASSION
    __MARKER_ID = BATTLE_MARKER_STATES.SHOT_PASSION_STATE
    def __init__(self):
        ...
    def set_stage(self, prev):
        ...
    def getInfo(self):
        ...
    def _updateTimer(self, data):
        ...
    def _getDuration(self):
        ...
