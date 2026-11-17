# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleFireCircleEffectComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as BATTLE_MARKER_STATES
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent as VehicleAbilityBaseComponent
from items import vehicles as vehicles
from shared_utils import first as first
from battle_royale_artefacts import FireCircle as FireCircle

class VehicleFireCircleEffectComponent(VehicleAbilityBaseComponent):
    __CLASS_NAME = 'VehicleFireCircleEffectComponent'
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.FIRE_CIRCLE
    __MARKER_ID = BATTLE_MARKER_STATES.FIRE_CIRCLE_STATE
    def __init__(self):
        ...
    def _getDuration(self):
        ...
    @staticmethod
    def getEquipment():
        ...
    def _destroy(self):
        ...
