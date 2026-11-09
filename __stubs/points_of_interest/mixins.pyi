# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/points_of_interest/mixins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
from gui.battle_control import avatar_getter as avatar_getter
from points_of_interest.components import PoiStateComponent as PoiStateComponent, PoiStateUIListenerComponent as PoiStateUIListenerComponent
from points_of_interest.managers import PoiStateCreateSystem as PoiStateCreateSystem
from shared_utils import first as first

class PointsOfInterestListener(object):
    __listenerGameObject: Any
    def __init__(self):
        ...
    def onPoiAdded(self, poiState):
        ...
    def onPoiRemoved(self, poiState):
        ...
    def onProcessPoi(self, poiState):
        ...
    def onPoiEntered(self, poiID):
        ...
    def onPoiLeft(self, poiID):
        ...
    @property
    def _poiStateSystem(self):
        ...
    @property
    def _poiStateQuery(self):
        ...
    @property
    def _poiVehicleState(self):
        ...
    def _registerPoiListener(self, go=None):
        ...
    def _unregisterPoiListener(self, go=None):
        ...
