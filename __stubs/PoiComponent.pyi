# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PoiComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import typing as typing
import CGF as CGF
import GenericComponents as GenericComponents
import Math as Math
from typing import List as List
from helpers import dependency as dependency, fixed_dict as fixed_dict
from points_of_interest.components import PoiStateComponent as PoiStateComponent
from points_of_interest_shared import PoiType as PoiType, PoiStatus as PoiStatus
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class PoiComponent(DynamicScriptComponent):
    __sessionProvider: Any
    __dynObjectsCache: Any
    __prefabGo: Any
    def __init__(self):
        ...
    @property
    def _poiVisualConfig(self):
        ...
    def onDestroy(self):
        ...
    def set_progress(self, prev):
        ...
    def set_invader(self, prev):
        ...
    def set_status(self, prev):
        ...
    def _onAvatarReady(self):
        ...
    def __createVisual(self):
        ...
    def __removeVisual(self):
        ...
    def __onPrefabLoaded(self, objects, queue):
        ...
    def __updateRadius(self, root, queue):
        ...
    def __getStatus(self):
        ...
