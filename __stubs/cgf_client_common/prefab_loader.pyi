# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/cgf_client_common/prefab_loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
from cgf_client_common.game_object_holder import GameObjectHolder as GameObjectHolder

class PrefabLoader(GameObjectHolder):
    _loadingQueue: Any
    __prefabLoadRequests: Any
    def __init__(self, spaceID, gameObjectName=None):
        ...
    def isReady(self):
        ...
    def _destroy(self, queue=None):
        ...
    def loadPrefab(self, prefab, go, vector, callback):
        ...
    def _flushLoadingQueue(self):
        ...
    def _clearLoadingQueue(self):
        ...
    def __startPrefabLoad(self, prefab, go, vector, callback):
        ...
    def _cancelPrefabLoadRequests(self):
        ...
