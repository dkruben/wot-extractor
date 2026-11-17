# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VisualScriptEquipment.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import EQUIPMENT_STAGES as STAGES
from helpers import dependency as dependency
from helpers.fixed_dict import getVisualScriptEquipmentState as getVisualScriptEquipmentState
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from visual_script.misc import ASPECT as ASPECT
from visual_script_client.contexts.ability_context import AbilityContextClient as AbilityContextClient
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent

class VisualScriptEquipment(DynamicScriptComponent):
    __sessionProvider: Any
    _vsPlan: Any
    _context: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def canActivate(self):
        ...
    def onDestroy(self):
        ...
    def set_errorState(self, _=None):
        ...
    def set_equipmentState(self, _=None):
        ...
    def update(self):
        ...
    def __update(self, state):
        ...
