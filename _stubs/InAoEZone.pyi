# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/InAoEZone.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from wotdecorators import noexcept as noexcept

class InAoEZone(BigWorld.DynamicScriptComponent):
    __guiSessionProvider: Any
    def __init__(self):
        ...
    # decorador original: @noexcept
    def setSlice_inAoEZoneData(self, path, old):
        ...
    def isVehicleInActiveZone(self):
        ...
