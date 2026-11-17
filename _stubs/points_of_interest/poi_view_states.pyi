# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/points_of_interest/poi_view_states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import CGF as CGF
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from points_of_interest.components import PoiStateComponent as PoiStateComponent, PoiCaptureBlockerStateComponent as PoiCaptureBlockerStateComponent
PointViewState: Any
VehicleViewState: Any
StateComponent: Any
ViewState: Any

class _ViewStateUpdater(object):
    __guiSessionProvider: Any
    __stateUUID: Any
    __viewState: Any
    def __init__(self, stateUUID):
        ...
    def getState(self, statesAccess):
        ...
    def update(self, statesAccess):
        ...
    def clear(self):
        ...
    @staticmethod
    def _getViewStateID():
        ...
    @staticmethod
    def _getViewState(state):
        ...
    def __invalidateViewState(self):
        ...

class PointViewStateUpdater(_ViewStateUpdater):
    @staticmethod
    def _getViewStateID():
        ...
    @staticmethod
    def _getViewState(state):
        ...

class VehicleViewStateUpdater(_ViewStateUpdater):
    @staticmethod
    def _getViewStateID():
        ...
    @staticmethod
    def _getViewState(state):
        ...
