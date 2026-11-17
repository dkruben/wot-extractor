# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffPanelComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from dyn_components_groups import groupComponent as groupComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from xml_config_specs import StrParam as StrParam
from constants import ARENA_BONUS_TYPE_IDS as ARENA_BONUS_TYPE_IDS

# decorador original: @groupComponent(...)
class HWBuffPanelComponent(DynamicScriptComponent):
    guiSessionProvider: Any
    _buffKey: Any
    _showNotificationPopup: Any
    def __init__(self):
        ...
    @property
    def buffKey(self):
        ...
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
