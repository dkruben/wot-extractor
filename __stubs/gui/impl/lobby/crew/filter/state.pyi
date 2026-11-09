# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/filter/state.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import Iterable as Iterable, defaultdict as defaultdict
from account_helpers.AccountSettings import AccountSettings as AccountSettings, TANKMEN_LIST as TANKMEN_LIST
from Event import Event as Event
from gui.impl.gen.view_models.views.lobby.crew.common.filter_toggle_group_model import ToggleGroupType as ToggleGroupType

class FilterState(object):
    GROUPS = ToggleGroupType
    onStateChanged: Any
    _state: Any
    _initialState: Any
    __searchString: Any
    _isWotPlus: Any
    _persistor: Any
    def __init__(self, initialState=None, isWotPlus=False, persistor=None):
        ...
    def __contains__(self, item):
        ...
    def __getitem__(self, item):
        ...
    def __iter__(self):
        ...
    def __repr__(self):
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
    def _clear(self):
        ...

class Persistor(object):
    __key: Any
    __persistentGroups: Any
    __excludeKeys: Any
    __ignoreDefault: Any
    def __init__(self, storageKey, persistentGroups=None, excludeKeys=None, ignoreDefault=False):
        ...
    def __repr__(self):
        ...
    def load(self, stateDict):
        ...
    def save(self, stateDict):
        ...
    def __storableState(self, stateDict):
        ...
