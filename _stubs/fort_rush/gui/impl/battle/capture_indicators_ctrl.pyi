# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/battle/capture_indicators_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers.events_handler import EventsHandler as EventsHandler
from typing import TYPE_CHECKING as TYPE_CHECKING
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_base_capture_indicator_model import FortRushHudBaseCaptureIndicatorModel as FortRushHudBaseCaptureIndicatorModel, FortRushBaseCaptureState as FortRushBaseCaptureState
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_base_marker_model import FortRushHudBaseMarkerModel as FortRushHudBaseMarkerModel
from fort_rush.gui.shared.events import CapturePointEvent as CapturePointEvent
from fort_rush.gui.shared.team_utils import getTeamValue as getTeamValue
from fort_rush_common.component_helpers import getInvaderComponent as getInvaderComponent
from fort_rush_common.fort_rush_constants import CaptureStates as CaptureStates
from gui.battle_control import avatar_getter as avatar_getter
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, EventPriority as EventPriority
from frameworks.wulf import Array as Array, Map as Map
INVALID_CAPTURE_POINT_UID = -1
CAPTURE_STATE_TO_ENUM: dict

class CaptureIndicatorsCtrl(EventsHandler):
    __hudRef: Any
    def __init__(self, hudRef):
        ...
    def init(self):
        ...
    def dispose(self):
        ...
    def _getListeners(self):
        ...
    @property
    def _capturablePointsByUid(self):
        ...
    @property
    def _capturePointsMarkerArray(self):
        ...
    def _createCapturablePointModel(self, uid, capturablePointName):
        ...
    def _createCapturablePointMarkerModel(self, data):
        ...
    def _getCapturablePointModel(self, uid, capturablePointName):
        ...
    def _getCapturablePointMarkerModel(self, data):
        ...
    def _updateCapturePointModel(self, event):
        ...
    def _initCapturablePointMarker(self, event):
        ...
    def _findUidByLabel(self, capturablePointName):
        ...
    def _updateProgressBar(self, incomingState):
        ...
