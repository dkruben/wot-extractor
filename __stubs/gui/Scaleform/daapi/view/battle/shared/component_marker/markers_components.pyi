# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/component_marker/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import math as math
import weakref as weakref
from past.utils import old_div as old_div
import AnimationSequence as AnimationSequence
import BigWorld as BigWorld
import Math as Math
from account_helpers.settings_core.settings_constants import BattleCommStorageKeys as BattleCommStorageKeys
from chat_commands_consts import INVALID_TARGET_ID as INVALID_TARGET_ID, MarkerType as MarkerType
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from account_helpers.settings_core import ISettingsCore as ISettingsCore, settings_constants as settings_constants
from helpers import dependency as dependency
from shared_utils import BitmaskHelper as BitmaskHelper
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from gui.Scaleform.daapi.view.battle.shared import indicators as indicators
from gui.Scaleform.daapi.view.battle.shared.markers2d.markers import ReplyStateForMarker as ReplyStateForMarker
from gui.Scaleform.daapi.view.battle.shared.indicators import _DIRECT_INDICATOR_SWF as SWF, _DIRECT_INDICATOR_MC_NAME as MC_NAME
from gui.Scaleform.daapi.view.battle.shared.markers2d.settings import MARKER_SYMBOL_NAME as MARKER_SYMBOL_NAME, CommonMarkerType as CommonMarkerType
from gui.impl import backport as backport
from gui.impl.gen import R as R
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
import CombatSelectedArea as CombatSelectedArea
from gui.battle_control import minimap_utils as minimap_utils
import ResMgr as ResMgr
_logger: Any
COMPONENT_MARKER_TYPE_NAMES: dict
COMPONENT_MARKER_TYPE_IDS: dict

class Blending(object):
    NORMAL = 'normal'
    ADD = 'add'
    MULTIPLY = 'multiply'
    SCREEN = 'screen'
    SUBTRACT = 'subtract'

class ComponentBitMask(BitmaskHelper):
    NONE = 0
    MARKER_2D = 1
    MINIMAP_MARKER = 2
    DIRECTION_INDICATOR = 4
    ANIM_SEQUENCE_MARKER = 8
    TERRAIN_MARKER = 16
    FULLSCREEN_MAP_MARKER = 32
    LIST: tuple

class _IMarkerComponentBase(object):
    settingsCore: Any
    _idGen: Any
    _componentID: Any
    _config: Any
    _matrixProduct: Any
    _isVisible: Any
    _targetID: Any
    _entity: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @property
    def isVisible(self):
        ...
    @property
    def componentID(self):
        ...
    @property
    def position(self):
        ...
    @property
    def positionWithOffset(self):
        ...
    @property
    def maskType(self):
        ...
    @property
    def bcMarkerType(self):
        ...
    def update(self, *args, **kwargs):
        ...
    def clear(self):
        ...
    def setVisible(self, isVisible):
        ...
    def attachGUI(self, guiProvider, **kwargs):
        ...
    def detachGUI(self):
        ...
    def setMarkerMatrix(self, matrix):
        ...
    def setMarkerEntity(self, entity):
        ...
    def setMarkerPosition(self, position):
        ...
    @classmethod
    def configReader(cls, section):
        ...

class World2DMarkerComponent(_IMarkerComponentBase):
    _METERS_STRING: Any
    _gui: Any
    _isMarkerExists: Any
    _displayDistance: Any
    _distance: Any
    _symbol: Any
    _isVisible: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def maskType(self):
        ...
    @property
    def guiMarkerType(self):
        ...
    @property
    def symbol(self):
        ...
    def attachGUI(self, guiProvider, **kwargs):
        ...
    def detachGUI(self):
        ...
    def clear(self):
        ...
    def setVisible(self, isVisible):
        ...
    def update(self, distance, *args, **kwargs):
        ...
    def setMarkerMatrix(self, matrix):
        ...
    def _createMarker(self, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _onSettingsChanged(self, diff):
        ...

class World2DActionMarkerComponent(World2DMarkerComponent):
    MARKER_CULL_DISTANCE = 1800
    MARKER_MIN_SCALE = 60.0
    MARKER_BOUNDS: Any
    MARKER_INNER_BOUNDS: Any
    MARKER_BOUND_MIN_SCALE: Any
    _isStickyFromConfig: Any
    _isMarkerExists: Any
    _isVisible: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def guiMarkerType(self):
        ...
    @property
    def bcMarkerType(self):
        ...
    @property
    def symbol(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _onSettingsChanged(self, diff):
        ...

class World2DLocationMarkerComponent(World2DMarkerComponent):
    CULL_DISTANCE = 1800
    MIN_SCALE = 50.0
    BOUNDS: Any
    INNER_BOUNDS: Any
    BOUNDS_MIN_SCALE: Any
    MIN_Y_OFFSET = 1.2
    MAX_Y_OFFSET = 3.2
    DISTANCE_FOR_MIN_Y_OFFSET = 400
    MAX_Y_BOOST = 1.4
    BOOST_START = 120
    _isStickyFromConfig: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def guiMarkerType(self):
        ...
    @property
    def bcMarkerType(self):
        ...
    @property
    def symbol(self):
        ...
    def update(self, distance, *args, **kwargs):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _onSettingsChanged(self, diff):
        ...

class BaseMinimapMarkerComponent(_IMarkerComponentBase):
    _gui: Any
    _isMarkerExists: Any
    _onlyTranslation: Any
    _translationOnlyMP: Any
    _isVisible: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def maskType(self):
        ...
    def attachGUI(self, guiProvider, **kwargs):
        ...
    def detachGUI(self):
        ...
    def clear(self):
        ...
    def setVisible(self, isVisible):
        ...
    def _createMarker(self, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def update(self, *args, **kwargs):
        ...
    def setMarkerMatrix(self, matrix):
        ...
    def _getPlugin(self, guiProvider):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

class MinimapMarkerComponent(BaseMinimapMarkerComponent):
    @property
    def maskType(self):
        ...

class FullscreenMapComponent(BaseMinimapMarkerComponent):
    @property
    def maskType(self):
        ...

class DirectionIndicatorMarkerComponent(_IMarkerComponentBase):
    _DIRECT_INDICATOR_SWF = SWF
    _DIRECT_INDICATOR_MC_NAME = MC_NAME
    __shapes: Any
    __indicator: Any
    __prevPosition: Any
    __swf: Any
    __mcName: Any
    _isVisible: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def maskType(self):
        ...
    def attachGUI(self, _, **kwargs):
        ...
    def detachGUI(self):
        ...
    def update(self, distance, *args, **kwargs):
        ...
    def clear(self):
        ...
    def setVisible(self, isVisible):
        ...
    def __updateVisibility(self):
        ...
    @property
    def __currentShape(self):
        ...
    def __onSettingsChanged(self, diff):
        ...

class AnimationSequenceMarkerComponent(_IMarkerComponentBase):
    __path: Any
    __animator: Any
    __spaceID: Any
    _isVisible: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def maskType(self):
        ...
    def clear(self):
        ...
    def update(self, *args, **kwargs):
        ...
    def setVisible(self, isVisible):
        ...
    def __onSequenceLoaded(self, resourceRefs):
        ...

class TerrainMarkerComponent(_IMarkerComponentBase):
    DEF_SIZE: tuple
    DEF_DIRECTION: Any
    DEF_COLOR = CombatSelectedArea.COLOR_WHITE
    __area: Any
    __direction: Any
    __objDirection: Any
    __prevPosition: Any
    _isVisible: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def maskType(self):
        ...
    def clear(self):
        ...
    def update(self, *args, **kwargs):
        ...
    def setVisible(self, isVisible):
        ...

class PolygonalZoneMinimapMarkerComponent(MinimapMarkerComponent):
    _polygon: Any
    _isBorderVisible: Any
    _maskingPolygons: Any
    _properties: Any
    _isVisible: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def isVisible(self):
        ...
    def getPolygon(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def detachGUI(self):
        ...
    def update(self, *args, **kwargs):
        ...
    def setVisible(self, isVisible):
        ...
    def _addMask(self, guid):
        ...
    def _initPolygon(self):
        ...
    def _fillMaskingPolygons(self, mask, xc, yc):
        ...
    def _getSize(self):
        ...
    def _updatePolygon(self):
        ...
    def _updateMasks(self):
        ...
    def _getGradientSize(self):
        ...
    def __getMarkerProperties(self, isColorBlind):
        ...
    def __isColorBlind(self):
        ...
    def __onSettingsChanged(self, diff):
        ...

class StaticDeathZoneMinimapMarkerComponent(PolygonalZoneMinimapMarkerComponent):
    @property
    def isVisible(self):
        ...
    def getPolygon(self):
        ...

class W2GTBattleZoneMinimapMarkerComponent(MinimapMarkerComponent):
    FILL_COLOR = '0xffdd99'
    FILL_ALPHA = 0.5
    OUTLINE_THICKNESS = 1.0
    OUTLINE_COLOR = '0xffdd99'
    OUTLINE_ALPHA = 1.0
    DOT_RADIUS = 1.0
    DOT_GAP = 2.0
    __polygon: Any
    __isHighlight: Any
    __isActive: Any
    __colorSection: Any
    __state: Any
    __isVisible: Any
    _properties: Any
    _states: Any
    class OutlineStyle(object):
        SOLID = 'solid'
        DOTTED = 'dotted'
    class Colors(object):
        DEFAULT = 'color'
        BLIND = 'colorBlind'
        ALL: tuple
    class ZoneState(object):
        DEFAULT = 'default'
        ACTIVE = 'active'
        HIGHLIGHT = 'highlight'
        ALL: tuple
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @property
    def bcMarkerType(self):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    def highlightZone(self, isHighlight):
        ...
    def activeZone(self, isActive):
        ...
    def changeVisibility(self, isVisible):
        ...
    def detachGUI(self):
        ...
    def setVisible(self, isVisible):
        ...
    def _setupMarker(self, gui, polygon=None, zoneType='', icon='empty', iconX=0, iconY=0, **kwargs):
        ...
    def _initPolygon(self, polygon):
        ...
    def _getSize(self):
        ...
    def _setupPolygon(self):
        ...
    def __setIcon(self, icon, iconX, iconY):
        ...
    def __getMarkerProperties(self, colorSection, state):
        ...
    def __getState(self):
        ...
    def __isColorBlind(self):
        ...
    def __updateColorsProperties(self):
        ...
    def __updateState(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __isPolygonValid(self, polygon):
        ...

def _getDirectionIndicator(swf, mcName):
    ...
