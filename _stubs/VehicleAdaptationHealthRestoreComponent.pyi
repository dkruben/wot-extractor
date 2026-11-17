# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/VehicleAdaptationHealthRestoreComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent as VehicleAbilityBaseComponent
from items import vehicles as vehicles
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from battle_royale_artefacts import AdaptationHealthRestore as AdaptationHealthRestore

class VehicleAdaptationHealthRestoreComponent(VehicleAbilityBaseComponent):
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.ADAPTATION_HEALTH_RESTORE
    __MARKER_ID = BATTLE_MARKER_STATES.ADAPTATION_HEALTH_RESTORE_STATE
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_restoreHealth(self, _=None):
        ...
    def _getDuration(self):
        ...
    @staticmethod
    def getEquipment():
        ...
