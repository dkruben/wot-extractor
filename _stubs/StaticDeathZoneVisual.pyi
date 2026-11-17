# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/StaticDeathZoneVisual.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import BigWorld as BigWorld
import math as math
from Math import Vector3 as Vector3, Vector4 as Vector4
from Event import Event as Event
from helpers import dependency as dependency
from gui.shared import g_eventBus as g_eventBus
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.doc_loaders import GuiColorsLoader as GuiColorsLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core import settings_constants as settings_constants
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent

class _DrawType(enum.IntEnum):
    NORMAL = 0
    STRIPES = 1

class StaticDeathZoneVisual(DynamicScriptComponent):
    sessionProvider: Any
    settingsCore: Any
    onShowDeathZone: Any
    onHideDeathZone: Any
    _borders: Any
    _borderDrawType: Any
    _visible: Any
    _rotation: Any
    deathzone_size: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def show(self):
        ...
    def hide(self):
        ...
    def getClosestPoint(self, point, _):
        ...
    def getClosestPointInverted(self, point, _):
        ...
    def getPolygon(self):
        ...
    def getDimensions(self):
        ...
    def resize(self, position, size, rotation):
        ...
    def _onAvatarReady(self):
        ...
    def _onEntityActiveChanged(self, isActive):
        ...
    def _removeBorders(self):
        ...
    def _drawBorders(self):
        ...
    def _hideBorders(self):
        ...
    def _updateBorderDrawType(self, arenaDrawType):
        ...
    def _onArenaBorderTypeChanged(self, event):
        ...
    @property
    def _spaceID(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __getCurrentColor(self, colorBlind):
        ...

class _BordersHelper(object):
    _bounds: Any
    _min: Any
    _max: Any
    _center: Any
    _rotation: Any
    _polygon: Any
    _halfSize: Any
    _cos: Any
    _sin: Any
    def __init__(self):
        ...
    def init(self, center, size, rotation):
        ...
    def getClosestPoint(self, point):
        ...
    def getClosestPointInverted(self, point):
        ...
    @property
    def polygon(self):
        ...
    @property
    def bounds(self):
        ...

class _BordersHelperCircle(_BordersHelper):
    _EPSILON = 0.01
    _centerX: Any
    _centerZ: Any
    _R: Any
    def __init__(self):
        ...
    def init(self, center, size, rotation):
        ...
    def getClosestPoint(self, point):
        ...
    def getClosestPointInverted(self, point):
        ...
