# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/overlay.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
import GUI as GUI
from wg_async import wg_async as wg_async, wg_await as wg_await, AsyncEvent as AsyncEvent
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.lobby_entry import LobbyEntry as LobbyEntry
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents, CameraMovementStates as CameraMovementStates
from gui.shared import g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IOverlayController as IOverlayController, IHeroTankController as IHeroTankController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_ANIMATION_DURATION = 300
_LAYERS: tuple

class OverlayController(IOverlayController):
    _hangarSpace: Any
    _appLoader: Any
    _heroTankCtrl: Any
    _c11n: Any
    _selectableObjectsPrevState: Any
    _stateOn: Any
    _stateInProgess: Any
    _backgroundAlpha: Any
    _optimizationEnabled: Any
    _globalBlur: Any
    _wasBlurEnabled: Any
    _showEvent: Any
    _cameraState: Any
    __previouslyVisibleLayers: Any
    onStateChanged: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    # decorador original: @wg_async
    def waitShow(self):
        ...
    @property
    def isActive(self):
        ...
    def setOverlayState(self, state):
        ...
    @property
    def _guiState(self):
        ...
    def _changeGUIVisibility(self):
        ...
    def _restoreGraphics(self):
        ...
    def _onCameraEntityUpdated(self, event):
        ...
    def _canShow(self):
        ...
