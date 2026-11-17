# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/updaters_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer

class IViewUpdater(object):
    def initialize(self):
        ...
    def finalize(self):
        ...
    def destroy(self):
        ...

class ViewUpdatersCollection(object):
    __updaters: Any
    def __init__(self):
        ...
    def initialize(self, updaters):
        ...
    def finalize(self):
        ...
    def destroy(self):
        ...

class ViewUpdater(ClientEventsContainer, IViewUpdater):
    __view: Any
    def __init__(self, view):
        ...
    @property
    def view(self):
        ...
    def destroy(self):
        ...
