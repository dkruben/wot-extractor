# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSVehicleInvulnerableMarkerComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID

class LSVehicleInvulnerableMarkerComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def showNoHitMarker(self, attackerID):
        ...
