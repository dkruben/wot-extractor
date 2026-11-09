# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_parallax.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Math as Math
import GUI as GUI
import BigWorld as BigWorld
import Windowing as Windowing
import Keys as Keys
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer, TimeDeltaMeter as TimeDeltaMeter
import math_utils as math_utils
from account_helpers.settings_core.settings_constants import GAME as GAME
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from helpers import dependency as dependency
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui import g_keyEventHandlers as g_keyEventHandlers

class HangarCameraParallax(CallbackDelayer, TimeDeltaMeter):
    CURSOR_POSITION_CLAMP_VALUE = 2.0
    MAX_DT = 0.05
    settingsCore: Any
    __camera: Any
    __isInIdle: Any
    __smoothedCursorPosition: Any
    __wasPreviousUpdateSkipped: Any
    __distanceDelta: Any
    __anglesDelta: Any
    __smoothingMultiplier: Any
    __isEnabled: Any
    __isWindowAccessible: Any
    __isMouseDown: Any
    __isActive: Any
    __isInitialized: Any
    def __init__(self, camera):
        ...
    def destroy(self):
        ...
    def initialize(self, distanceDelta, angelsDelta, smoothing):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def isActive(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def onWindowAccessibilityChanged(self, isAccessible):
        ...
    def setEnabled(self, isEnabled=True):
        ...
    def __handleKeyEvent(self, event):
        ...
    def __checkToSkipUpdate(self):
        ...
    def __getClampedCursor(self):
        ...
    def __update(self):
        ...
    def __handleIdleCameraActivation(self, event):
        ...
    def __onForceDisable(self, event):
        ...

def cubicEasing(delta, position):
    ...
def linearEasing(delta, position):
    ...
