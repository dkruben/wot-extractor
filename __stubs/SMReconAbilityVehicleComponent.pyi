# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/SMReconAbilityVehicleComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
from gui.impl.gen import R as R
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from story_mode_common.story_mode_constants import RECON_ABILITY as RECON_ABILITY, EQUIPMENT_STAGES as STAGES
from gui.battle_control.controllers.consumables.equipment_ctrl import _EquipmentItem as _EquipmentItem

class SMReconAbilityVehicleComponent(DynamicScriptComponent):
    _EQUIPMENT_NAME = RECON_ABILITY
    onSMReconAbilityActivated: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def _onEquipmentUpdated(self, _, item):
        ...
