# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/py2to3/patched_typing.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import abc as abc
import typing as typing
from future.utils import PY2 as PY2
__all__: tuple

class _RuntimeGenericMeta(abc.ABCMeta):
    def __getitem__(cls, item):
        ...

class Generic(object, metaclass=_RuntimeGenericMeta):
    __slots__: tuple
