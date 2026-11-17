# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/cgf/capture_point.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
import CGF as CGF
import DebugDrawer as DebugDrawer
import Math as Math
from CapturePointComponent import CapturePointComponent as CapturePointComponent, CapturePointMarkerAnchor as CapturePointMarkerAnchor
from GenericComponents import Sequence as Sequence
from cgf_modules.variable_components import VariableStorageComponent as VariableStorageComponent
from constants import IS_CLIENT as IS_CLIENT
from fort_rush.gui.shared.events import CapturePointEvent as CapturePointEvent
from fort_rush.helpers.utils import getCurrentTeam as getCurrentTeam
from fort_rush_common.fort_rush_constants import CAPTURE_POINT_NO_TEAM as CAPTURE_POINT_NO_TEAM
from fort_rush_common.fort_rush_constants import CaptureStates as CaptureStates
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
INVALID_CAPTURE_POINT_UID = -1
_logger: Any
MARKER_ANCHOR_GIZMO_COLOUR = 13385641
MARKER_ANCHOR_GIZMO_SCALE: Any
COMPATIBLE_VFX_STATES: tuple

class ZoneVFXStates(object):
    DEFAULT = 1
    NEUTRAL = 2
    ALLY_CAPTURED = 3
    ENEMY_CAPTURED = 4
    ALLY_CONTESTED = 5
    ENEMY_CONTESTED = 6
    CONTESTED_TO_ALLY = 7
    CONTESTED_TO_ENEMY = 8

class CapturePointSystem(CGF.System):
    Activated: Any
    Removed: Any
    VariableStorageAccess: Any
    SequenceAccess: Any
    MarkerAnchorAccess: Any
    Reactions: Any
    _delayer: Any
    def __init__(self):
        ...
    def onMappingUnloaded(self):
        ...
    def update(self):
        ...
    def onActivate(self, go, capturePointComponent, transform):
        ...
    def _dispatchInitEvent(self, go, capturePointComponent, transform):
        ...
    def _findMarkerAnchorTransform(self, go):
        ...
    def updateSequence(self, go, point, prevState):
        ...
    def _evaluateSequenceLayer(self, point, prevState):
        ...
    def _switchLayer(self, go, layerIndex):
        ...

class CapturePointMarkerAnchorGizmoSystem(CGF.System):
    MarkerAnchorsReaction: Any
    Reactions: Any
    def update(self):
        ...
