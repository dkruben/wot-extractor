# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/crosshair_proxy.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import GUI as GUI
import Event as Event
import aih_constants as aih_constants
import BattleReplay as BattleReplay
from AvatarInputHandler import aih_global_binding as aih_global_binding
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID, STRATEGIC_CAMERA_ID as STRATEGIC_CAMERA_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_BINDING_ID = aih_global_binding.BINDING_ID
_CTRL_MODE = aih_constants.CTRL_MODE_NAME
_MARKER_TYPE = aih_constants.GUN_MARKER_TYPE
_MARKER_FLAG = aih_constants.GUN_MARKER_FLAG
_STRATEGIC_CAMERA = aih_constants.STRATEGIC_CAMERA
_CTRL_MODE_TO_VIEW_ID: dict
_GUN_MARKERS_SET_IDS: tuple
_STRATEGIC_CAMERA_TO_ID: dict

class GunMarkersSetInfo(object):
    clientMarkerDataProvider: Any
    clientSPGMarkerDataProvider: Any
    serverMarkerDataProvider: Any
    serverSPGMarkerDataProvider: Any
    dualAccMarkerDataProvider: Any
    __gunMarkersFlags: Any
    @property
    def isClientMarkerActivated(self):
        ...
    @property
    def isServerMarkerActivated(self):
        ...
    @property
    def isEnabledInVideoMode(self):
        ...
    @property
    def isArtyHitActivated(self):
        ...
    def __isFlagActivated(self, flag):
        ...

class CrosshairDataProxy(IBattleController):
    __slots__: tuple
    settingsCore: Any
    __spgShotsIndicatorState: Any
    __multiGunCollisions: Any
    __ctrlMode: Any
    __offset: Any
    __zoomFactor: Any
    __width: Any
    __height: Any
    __positionX: Any
    __positionY: Any
    __scale: Any
    __viewID: Any
    __strategicCameraID: Any
    __eManager: Any
    onCrosshairViewChanged: Any
    onCrosshairOffsetChanged: Any
    onCrosshairSizeChanged: Any
    onCrosshairPositionChanged: Any
    onCrosshairScaleChanged: Any
    onCrosshairZoomFactorChanged: Any
    onGunMarkerStateChanged: Any
    onMultiGunCollisionsUpdated: Any
    onGunMarkersSetChanged: Any
    onStrategicCameraChanged: Any
    onSPGShotsIndicatorStateChanged: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getViewID(self):
        ...
    def getSize(self):
        ...
    def getPosition(self):
        ...
    def getScaledPosition(self):
        ...
    def getDisaredPosition(self):
        ...
    def getScaleFactor(self):
        ...
    def getOffset(self):
        ...
    def getZoomFactor(self):
        ...
    def getStrategicCameraID(self):
        ...
    @staticmethod
    def getGunMarkersSetInfo():
        ...
    def getMultiGunCollisions(self):
        ...
    def getSPGShotsIndicatorState(self):
        ...
    def __calculateSize(self, notify=True):
        ...
    def __calculatePosition(self, notify=True):
        ...
    def __setGunMarkerState(self, markerType, value):
        ...
    def __onAvatarControlModeChanged(self, ctrlMode):
        ...
    def __onAimOffsetChanged(self, offset):
        ...
    def __onScaleFactorChanged(self, scale):
        ...
    def __onClientGunMarkerStateChanged(self, value):
        ...
    def __onServerGunMarkerStateChanged(self, value):
        ...
    def __onMultiGunCollisionsUpdated(self, value):
        ...
    def __onZoomFactorChanged(self, zoomFactor):
        ...
    def __onGunMarkersSetChanged(self, *_):
        ...
    def __onSPGShotsIndicatorStateChanged(self, value):
        ...
    def __onStrategicCameraChanged(self, camera):
        ...

def getCrosshairViewIDByCtrlMode(ctrlMode):
    ...
