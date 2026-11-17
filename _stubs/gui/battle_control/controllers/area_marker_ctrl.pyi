# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/area_marker_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from helpers import dependency as dependency
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_controller import BaseMarkerController as BaseMarkerController
_logger: Any

class AreaMarkersController(BaseMarkerController):
    sessionProvider: Any
    _battleCtx: Any
    _arenaVisitor: Any
    def __init__(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def getPluginID(self):
        ...
    def spaceLoadCompleted(self):
        ...
    def _tickUpdate(self):
        ...
    def removeAllMarkers(self):
        ...
    def isMarkerActuallyVisible(self, marker):
        ...
    def _isMarkerActuallyVisibleImpl(self, marker, distanceToArea):
        ...
