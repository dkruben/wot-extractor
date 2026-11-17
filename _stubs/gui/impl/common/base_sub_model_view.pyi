# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/base_sub_model_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewModel as ViewModel
from py2to3 import patched_typing as patched_typing
TViewModel: Any

# base nao representavel no stub: patched_typing.Generic[...]
class BaseSubModelView(object):
    __slots__: tuple
    _viewModel: Any
    _isLoaded: Any
    def __init__(self, viewModel):
        ...
    def isLoaded(self):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def update(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
