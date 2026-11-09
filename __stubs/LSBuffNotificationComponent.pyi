# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSBuffNotificationComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from dyn_components_groups import groupComponent as groupComponent
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from xml_config_specs import StrParam as StrParam, ListParam as ListParam, ObjParam as ObjParam, FloatParam as FloatParam

# decorador original: @groupComponent(...)
class LSBuffNotificationComponent(DynamicScriptComponent):
    _sessionProvider: Any
    _buffKey: Any
    _params: Any
    def __init__(self):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    @property
    def buffKey(self):
        ...
    @property
    def params(self):
        ...
    def set_startTime(self, _):
        ...
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
