# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/markers_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
import SoundGroups as SoundGroups
import WWISE as WWISE
from typing import TYPE_CHECKING as TYPE_CHECKING
from StoryModeLootableComponent import StoryModeLootableComponent as StoryModeLootableComponent
from chat_commands_consts import MarkerType as MarkerType, INVALID_TARGET_ID as INVALID_TARGET_ID
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import PolygonalZoneMinimapMarkerComponent as PolygonalZoneMinimapMarkerComponent, World2DLocationMarkerComponent as World2DLocationMarkerComponent, BaseMinimapMarkerComponent as BaseMinimapMarkerComponent, ComponentBitMask as ComponentBitMask
from gui.Scaleform.daapi.view.battle.shared.minimap.settings import CONTAINER_NAME as CONTAINER_NAME, ENTRY_SYMBOL_NAME as ENTRY_SYMBOL_NAME, VIEW_RANGE_CIRCLES_AS3_DESCR as VIEW_RANGE_CIRCLES_AS3_DESCR, CIRCLE_STYLE as CIRCLE_STYLE
from gui.battle_control import minimap_utils as minimap_utils
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import time_utils as time_utils, dependency as dependency
from math_common import round_py2_style as round_py2_style
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from story_mode.gui.sound_constants import VDAY_LOOT_CAPTURE_COMPLETE_SOUND as VDAY_LOOT_CAPTURE_COMPLETE_SOUND, VDAY_LOOT_CAPTURE_PROGRESS_SOUND as VDAY_LOOT_CAPTURE_PROGRESS_SOUND, VDAY_LOOT_CAPTURE_RTPC as VDAY_LOOT_CAPTURE_RTPC, VDAY_LOOT_CAPTURE_START_SOUND as VDAY_LOOT_CAPTURE_START_SOUND, VDAY_LOOT_CAPTURE_STOP_SOUND as VDAY_LOOT_CAPTURE_STOP_SOUND
from story_mode_common.story_mode_constants import RECON_ABILITY as RECON_ABILITY
import ResMgr as ResMgr
from Math import Vector3 as Vector3
from gui.Scaleform.daapi.view.battle.shared.minimap.component import MinimapComponent as MinimapComponent

class SMPolygonalZoneMinimapMarkerComponent(PolygonalZoneMinimapMarkerComponent):
    def _getSize(self):
        ...

class PolygonalZoneFullScreenMapMarkerComponent(SMPolygonalZoneMinimapMarkerComponent):
    @property
    def maskType(self):
        ...

class LootMarkerComponent(World2DLocationMarkerComponent):
    _tickTimerId: Any
    _startTime: Any
    _captureTime: Any
    _isStickyFromConfig: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def bcMarkerType(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...
    def _onStartCapturing(self, startTime, captureTime):
        ...
    def _tick(self):
        ...
    def _onStopCapturing(self):
        ...
    def _cancelTimer(self):
        ...
    def clear(self):
        ...

class LootMinimapComponent(BaseMinimapMarkerComponent):
    @classmethod
    def configReader(cls, section):
        ...
    @property
    def maskType(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

class LootFullScreenMapComponent(LootMinimapComponent):
    @property
    def maskType(self):
        ...

class AbilityMinimapComponent(BaseMinimapMarkerComponent):
    @property
    def maskType(self):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

class AbilityFullScreenMapComponent(AbilityMinimapComponent):
    @property
    def maskType(self):
        ...

class AbilityReconMinimapComponent(AbilityMinimapComponent):
    _sessionProvider: Any
    _circlesID: Any
    def __init__(self, config, matrixProduct, entity=None, targetID=..., isVisible=True):
        ...
    def _createMarker(self, **kwargs):
        ...
    def _deleteMarker(self):
        ...
    def _addRangeCircle(self, position, viewRangeRadius):
        ...
    def _removeRangeCircle(self):
        ...
    def _applyScale(self, width, height):
        ...

class AbilityReconFullscreenMapComponent(AbilityReconMinimapComponent):
    MINIMAP_SIZE: tuple
    @property
    def maskType(self):
        ...
    def _applyScale(self, width, height):
        ...

class AbilityLocationMarkerComponent(World2DLocationMarkerComponent):
    @property
    def bcMarkerType(self):
        ...

class SMBitmapComponent(BaseMinimapMarkerComponent):
    @property
    def maskType(self):
        ...
    @classmethod
    def configReader(cls, section):
        ...
    def _setupMarker(self, gui, **kwargs):
        ...

class SMFullScreenMapBitmapComponent(SMBitmapComponent):
    @property
    def maskType(self):
        ...
