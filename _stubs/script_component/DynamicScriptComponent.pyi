# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/script_component/DynamicScriptComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import iteritems as iteritems
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from shared_utils import nextTick as nextTick
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
_logger: Any

class DynamicScriptComponent(BigWorld.DynamicScriptComponent):
    def __init__(self, *_, **__):
        ...
    @property
    def _isAvatarReady(self):
        ...
    def onDestroy(self):
        ...
    def onLeaveWorld(self):
        ...
    @property
    def spaceID(self):
        ...
    @property
    def keyName(self):
        ...
    def _onAvatarReady(self):
        ...
    def __onAvatarReady(self):
        ...
    @property
    def _isValid(self):
        ...
