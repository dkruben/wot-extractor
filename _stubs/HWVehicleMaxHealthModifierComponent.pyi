# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWVehicleMaxHealthModifierComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class HWVehicleMaxHealthModifierComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    @property
    def hwBattleGuiCtrl(self):
        ...
    def set_maxHealth(self, _):
        ...
