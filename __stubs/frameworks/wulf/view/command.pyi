# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/frameworks/wulf/view/command.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
from ..py_object_binder import PyObjectEntity as PyObjectEntity
from ..py_object_wrappers import PyObjectCommand as PyObjectCommand

class Command(PyObjectEntity):
    __slots__: tuple
    __event: Any
    def __init__(self):
        ...
    def __call__(self, args=None):
        ...
    @property
    def name(self):
        ...
    def execute(self, args=None):
        ...
    def _unbind(self):
        ...
    def _cNotify(self, args=None):
        ...
    def __iadd__(self, delegate):
        ...
    def __isub__(self, delegate):
        ...
