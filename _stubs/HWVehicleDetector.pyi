# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWVehicleDetector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import BigWorld as BigWorld
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class HWVehicleDetector(DynamicScriptComponent):
    guiSessionProvider: Any
    def onDestroy(self):
        ...
    def set_indicator(self, prev):
        ...
    def _onAvatarReady(self):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
    def _onCheckDistanceToFollower(self):
        ...
    def _onAvatarVehicleChanged(self):
        ...
    def __fireEvent(self, indicator=0):
        ...
