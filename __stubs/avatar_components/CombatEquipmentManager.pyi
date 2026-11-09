# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/CombatEquipmentManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import math as math
import SoundGroups as SoundGroups
import helpers as helpers
from future.utils import viewvalues as viewvalues
import math_utils as math_utils
import BigWorld as BigWorld
from Math import Vector2 as Vector2, Vector3 as Vector3
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
import BombersWing as BombersWing
import Flock as Flock
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
import CombatSelectedArea as CombatSelectedArea
from items import vehicles as vehicles
import BattleReplay as BattleReplay
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from math_common import round_py2_style as round_py2_style
from smoke_screen import SmokeScreen as SmokeScreen
_ENABLE_DEBUG_DRAW = False
_ENABLE_DEBUG_LOG = False

class _DebugFrontLine(CallbackDelayer):
    model: Any
    @staticmethod
    def launch(beginExplosionPos, endExplosionPos, areaWidth, velocity):
        ...
    def __init__(self, beginExplosionPos, endExplosionPos, areaWidth, velocity):
        ...
    def __onDeath(self):
        ...

class CombatEquipmentManager(object):
    guiSessionProvider: Any
    __callbackDelayer: Any
    __selectedAreas: Any
    __wings: Any
    __isGUIVisible: Any
    __lastSmokeInfo: Any
    __onCombatEquipmentShotCB: Any
    debugPolyLine: Any
    debugPoints: Any
    debugDirs: Any
    debugStartLine: Any
    debugEndLine: Any
    def testArtyStrike(self, strikeID=33, offset=...):
        ...
    def __init__(self):
        ...
    def onBecomePlayer(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomeNonPlayer(self):
        ...
    def updatePlaneTrajectory(self, planeTrajectory):
        ...
    def showHittingArea(self, equipmentID, pos, direction, time):
        ...
    def onCombatEquipmentShotLaunched(self, equipmentID, position):
        ...
    def __triggerOnCombatEquipmentShot(self, eventName, position):
        ...
    def __delayedAreaDestroy(self, areaUID):
        ...
    def __showMarkerCallback(self, eq, pos, direction, time, areaUID):
        ...
    def setGUIVisible(self, isVisible):
        ...
    def setVFXVisible(self, isVisible):
        ...
    @staticmethod
    def __calcBombsDistribution(bombsCnt, areaWidth, areaLength):
        ...
    def showCarpetBombing(self, equipmentID, pos, direction, time):
        ...
    def setEquipmentApplicationPoint(self, equipmentID, point, direction):
        ...
    @staticmethod
    def createEquipmentSelectedArea(pos, direction, equipment, areaSize=None):
        ...
    def onSmoke(self, smokeInfo):
        ...
    @property
    def lastSmokeInfo(self):
        ...
