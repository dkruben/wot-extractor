# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/cgf_client_common/game_object_holder.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF

class GameObjectHolder(object):
    _spaceID: Any
    __gameObjectName: Any
    _gameObject: Any
    def __init__(self, spaceID, gameObjectName=None):
        ...
    @property
    def gameObject(self):
        ...
    @property
    def spaceID(self):
        ...
    def _reset(self, queue=None):
        ...
    def _destroy(self, queue=None):
        ...
