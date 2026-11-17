# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/modification_cache/modification_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from collections import deque as deque
from typing import Optional as Optional, Any as Any

class ModificationCache(object):
    DEFAULT_LAYER_COUNT = 0
    __slots__: tuple
    _modifications: _Any
    _maxLayerCount: _Any
    _layerIdQueue: _Any
    def __init__(self, layerCount=None):
        ...
    def clear(self):
        ...
    def _addLayer(self, layerId, initValue=None):
        ...
