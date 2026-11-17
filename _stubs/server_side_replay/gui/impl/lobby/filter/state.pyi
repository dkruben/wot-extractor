# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/filter/state.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring, unicode as unicode
from py2to3.moves.collections.abc import Iterable as Iterable
from Event import Event as Event
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import ToggleGroupType as ToggleGroupType

class FilterState(object):
    GROUPS = ToggleGroupType
    onStateChanged: Any
    _state: Any
    __searchString: Any
    _initialState: Any
    isPrimeTime: Any
    lastDays: Any
    def __init__(self, initialState=None):
        ...
    def __contains__(self, item):
        ...
    def __getitem__(self, item):
        ...
    def __iter__(self):
        ...
    @property
    def searchString(self):
        ...
    @searchString.setter
    def searchString(self, value):
        ...
    @property
    def state(self):
        ...
    def clear(self):
        ...
    def update(self, groupID, fieldID):
        ...
    def reinit(self, state=None):
        ...
    def _reinitState(self, initialState=None):
        ...
    def __clear(self):
        ...
