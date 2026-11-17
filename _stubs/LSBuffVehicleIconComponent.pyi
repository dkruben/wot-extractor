# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSBuffVehicleIconComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from dyn_components_groups import groupComponent as groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from xml_config_specs import StrParam as StrParam
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID

# decorador original: @groupComponent(...)
class LSBuffVehicleIconComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    _icon: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    @property
    def icon(self):
        ...
