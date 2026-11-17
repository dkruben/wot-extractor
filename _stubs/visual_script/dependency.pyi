# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/dependency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import sys as sys
import typing as typing
from importlib import import_module as import_module
from constants import IS_VS_EDITOR as IS_VS_EDITOR
from py2to3.patched_future import with_metaclass as with_metaclass
from types import ModuleType as ModuleType
MOCK_IMPORT_ERRORS: list
__all__: tuple

class MockObjectMeta(type):
    def __getitem__(cls, item):
        ...
    def __getattr__(cls, item):
        ...
    def __iter__(cls):
        ...

# base nao representavel no stub: with_metaclass(...)
class MockObject:
    def __init__(self, *args, **kwargs):
        ...
    def __call__(self, *args, **kwargs):
        ...
    def __getitem__(self, item):
        ...
    def __getattr__(self, item):
        ...
    def __iter__(self):
        ...
    def __str__(self):
        ...

def tryImportGen(modules):
    ...
def dependencyImporter(*modules):
    ...
def dependencyMocker(*modules):
    ...
