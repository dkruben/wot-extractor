# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/base/state_machine/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import State as State
from enum import IntEnum as IntEnum

class BaseState(State):
    __slots__: tuple
    _view: Any
    _widgetType: Any
    _widgetId: Any
    def __init__(self, stateID, flags):
        ...
    def configure(self, view, widgetType, widgetId):
        ...
    def getSettings(self):
        ...
    def update(self):
        ...
    def _onEntered(self, event):
        ...
    def _showView(self):
        ...
    def _updateView(self):
        ...

class BaseTimerState(BaseState):
    __slots__: tuple
    _doUpdate: Any
    _doShow: Any
    def __init__(self, stateID, flags):
        ...
    def update(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def tick(self, currentTime):
        ...
