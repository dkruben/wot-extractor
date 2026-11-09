# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/LSBuffNitroComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from dyn_components_groups import groupComponent as groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from xml_config_specs import IntParam as IntParam
_NITRO_APPEARED = 1
_NITRO_HIDDEN = 0

# decorador original: @groupComponent(...)
class LSBuffNitroComponent(DynamicScriptComponent):
    _appearanceRef: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def _setType(self, nitro):
        ...
