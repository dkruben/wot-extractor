# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/component_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import weakref as weakref
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
from battleground.iself_assembler import ISelfAssembler as ISelfAssembler
from components_base.component_controller import ComponentController as ComponentController
from components_base.component_descriptor import ComponentDescriptorTyped as ComponentDescriptorTyped
from vehicle_systems import stricted_loading as stricted_loading

class Loader(object):
    resourceLoader: Any
    args: Any
    kwargs: Any
    def __init__(self, resourceLoader, *args, **kwargs):
        ...

class CompositeLoaderMixin(object):
    __pieces: Any
    __callback: Any
    def __init__(self):
        ...
    def prepareCompositeLoader(self, callback):
        ...
    def appendPiece(self, *_):
        ...
    def __invoke(self):
        ...
    def _piecesNum(self):
        ...

def loadComponentSystem(componentSystem, callback, resourceMapping=None, forceForegroundLoad=False):
    ...
def loadResourceMapping(resourceMapping, callback, *args, **kwargs):
    ...
def _processLoadedList(componentSystemWeak, callback, resourceMapping, resourceList):
    ...
