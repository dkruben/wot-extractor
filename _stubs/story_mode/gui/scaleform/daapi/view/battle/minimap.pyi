# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from story_mode.cgf_components.bunkers import BunkersSystem as BunkersSystem
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicTeleportPlugin as ClassicTeleportPlugin, ClassicMinimapPingPlugin as ClassicMinimapPingPlugin
from gui.Scaleform.daapi.view.battle.pve_base.minimap import PveMinimapComponent as PveMinimapComponent, PveMinimapGlobalSettingsPlugin as PveMinimapGlobalSettingsPlugin, PveScaleCenteredPersonalEntriesPlugin as PveScaleCenteredPersonalEntriesPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.common import SimplePlugin as SimplePlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.entries import VehicleEntry as VehicleEntry
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import ArenaVehiclesPlugin as ArenaVehiclesPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap.settings import CONTAINER_NAME as CONTAINER_NAME
from gui.battle_control import avatar_getter as avatar_getter, minimap_utils as minimap_utils
from gui.impl import backport as backport
from gui.impl.gen import R as R
from story_mode_common.story_mode_constants import VEHICLE_BUNKER_TURRET_TAG as VEHICLE_BUNKER_TURRET_TAG
_MINIMAP_DIMENSIONS = 10
_ANIMATION_SPG = 'enemySPG'
_ANIMATION_ENEMY = 'firstEnemy'
_BUNKER_SYMBOL = 'BunkerMinimapEntryUI'

class StoryModeVehicleEntry(VehicleEntry):
    __slots__: tuple
    def getSpottedAnimation(self, pool):
        ...

class StoryModeArenaVehiclesPlugin(ArenaVehiclesPlugin):
    __slots__: tuple
    def __init__(self, parent):
        ...
    def _skipMarker(self, vInfo, vProxy=None):
        ...

class BunkersPlugin(SimplePlugin):
    __slots__: tuple
    _DISTANCE_UPDATE_TIME = 1
    __bunkersDict: Any
    _distanceUpdateCallback: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def fini(self):
        ...
    def __onDestructibleEntityAdded(self, entity):
        ...
    def _updateDistanceToEntity(self, entityId, entity):
        ...
    def _distanceUpdate(self):
        ...
    def __onDestructibleEntityHealthChanged(self, destructibleEntityID, newHealth, maxHealth, atkID, atkReason, hitFlags):
        ...
    def __addBunkerEntry(self, position):
        ...

class StoryModeMinimapPingPlugin(ClassicMinimapPingPlugin):
    def _getClickPosition(self, x, y):
        ...

class StoryModePersonalEntriesPlugin(PveScaleCenteredPersonalEntriesPlugin):
    def _isInStrategicMode(self):
        ...

class StoryModeMinimapComponent(PveMinimapComponent):
    def _setupPlugins(self, arenaVisitor):
        ...
    def hasMinimapGrid(self):
        ...
    def getMinimapDimensions(self):
        ...
    def getBoundingBox(self):
        ...

def adjustBoundingBox(bl, tr):
    ...
