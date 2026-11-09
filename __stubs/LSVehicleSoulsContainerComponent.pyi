# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSVehicleSoulsContainerComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
from helpers import dependency as dependency
from last_stand_common.last_stand_constants import LSSoulsChangeReason as LSSoulsChangeReason
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class LSVehicleSoulsContainerComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    onChangeSoulsCount: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def set_lastCollected(self, _):
        ...
    def set_capacity(self, _):
        ...
    def onDestroy(self):
        ...
