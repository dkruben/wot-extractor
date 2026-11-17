# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWBuffDissolveComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from dyn_components_groups import groupComponent as groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from xml_config_specs import FloatParam as FloatParam
from functools import partial as partial
from math_utils import clamp as clamp, clamp01 as clamp01

class DissolveUpdater(object):
    __slots__: tuple
    UPDATE_RATE = 0.05
    dissolveHandler: Any
    componentRef: Any
    entityRef: Any
    appearanceRef: Any
    dissolveFactor: Any
    fadeInTime: Any
    fadeOutTime: Any
    maxDissolveFactor: Any
    dissolveFashions: Any
    compoundModel: Any
    def __init__(self, componentRef, entityRef, appearanceRef, dissolveFactor, fadeInTime, fadeOutTime, maxDissolveFactor):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _isTargetValid(self):
        ...
    @classmethod
    def _updateDissolve(cls, updater):
        ...

# decorador original: @groupComponent(...)
class HWBuffDissolveComponent(DynamicScriptComponent):
    def _onAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
