# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/uniprof/regions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import logging as logging
import BigWorld as BigWorld
_regions: dict
_logger: Any
_MAX_RGB_COLOR = 16581375

class _RegionDecorator(object):
    __slots__: tuple
    _label: Any
    _trackEnter: Any
    _trackExit: Any
    def __init__(self, label, trackEnter=False, trackExit=False):
        ...
    def __call__(self, func):
        ...
    def _enter(self):
        ...
    def _exit(self):
        ...

def _makeColorFromLabel(label):
    ...
def enterToRegion(label, color=None):
    ...
def exitFromRegion(label):
    ...
def regionDecorator(label, scope='wrap'):
    ...
