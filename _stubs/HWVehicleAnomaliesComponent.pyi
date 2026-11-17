# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWVehicleAnomaliesComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class HWVehicleAnomaliesComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    def set_usedAnomalies(self, _):
        ...
    def _notifyUsedAnomaliesChanged(self, usedAnomalies):
        ...
