# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/damage_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel as DamagePanel, _STATE_HANDLERS as _STATE_HANDLERS
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE

class HalloweenDamagePanel(DamagePanel):
    _prevFireStateValue: Any
    __prevDrainStateValue: Any
    def __init__(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
