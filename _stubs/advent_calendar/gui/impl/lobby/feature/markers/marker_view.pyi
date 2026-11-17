# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/markers/marker_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState as DoorState
from advent_calendar.gui.impl.gen.view_models.views.lobby.marker_view_model import MarkerViewModel as MarkerViewModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import getDoorState as getDoorState
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from gui.impl.gen import R as R
from gui.impl.lobby.common.hangar_marker_view import HangarMarkerView as HangarMarkerView
from helpers import dependency as dependency

class MarkerView(HangarMarkerView):
    _adventController: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _isVisible(self, doorsToOpenAmount):
        ...
    def _isAnimationEnabled(self):
        ...
    def _updateMarker(self, *args, **kwargs):
        ...
    def _getAvailableDoorsToOpenAmount(self):
        ...
