# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/BombersWing.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from collections import namedtuple as namedtuple
from future.utils import lmap as lmap, lzip as lzip
import AnimationSequence as AnimationSequence
import helpers as helpers
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from items import vehicles as vehicles
import BigWorld as BigWorld
from Math import Vector3 as Vector3
import SoundGroups as SoundGroups
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
CurveControlPoint: Any
BomberDesc: Any
AREA_LENGTH_SCALE_FACTOR = 0.05
_INITIAL_RETREAT_SHIFT = 200.0
_RETREAT_SUBDIVISION_FACTOR = 10
_MINIMAL_RETREAT_HEIGHT = 25
_MINIMAL_RETREAT_VELOCITY_FACTOR = 0.5
_GRAVITY = 9.81

class Bomber(object):
    ROLL_SPEED: Any
    timeOffset: Any
    motor: Any
    model: Any
    _desc: Any
    _model: Any
    __sound: Any
    _destroyed: Any
    __motor: Any
    def __init__(self, desc):
        ...
    def destroy(self):
        ...
    def startAttack(self, isAttacking):
        ...
    def setVisible(self, newVisible):
        ...
    def addControlPoint(self, position, velocity, time, attackEnded=False):
        ...
    def _loadRes(self):
        ...
    def _onAttackEnded(self, position, velocity):
        ...
    def _playSound(self):
        ...
    def _onModelLoaded(self, resourceRefs):
        ...
    def __onFlightStarted(self):
        ...

class CompoundBomber(Bomber):
    __flyAnimation: Any
    _model: Any
    _desc: Any
    def __init__(self, desc):
        ...
    def destroy(self):
        ...
    def tick(self, currentTime, timeDelta):
        ...
    def setTrigger(self, triggerName):
        ...
    def _loadRes(self):
        ...
    def _onAttackEnded(self, position, velocity):
        ...
    def _onModelLoaded(self, resourceRefs):
        ...
    def __onFlightStarted(self):
        ...

class BombersWing(CallbackDelayer):
    withdrawn: Any
    __withdrawn: Any
    __bombers: Any
    __equipment: Any
    __offsets: Any
    __fixedSpeed: Any
    __areaLength: Any
    def __init__(self, equipmentID, wingControlPoints):
        ...
    def destroy(self):
        ...
    def setVisible(self, newVisible):
        ...
    def __convertTime(self, time):
        ...
    def __calculateDirAndNorm(self, direction):
        ...
    def __calculateOffset(self, offset, flatDirAndNorm):
        ...
    def __calculateSpeed(self, start, finish):
        ...
    def __readData(self, equipmentID):
        ...
    def __onFlightComplete(self):
        ...
    def addControlPoint(self, curveControlPoints, bombing):
        ...
    def __generateRetreatTrajectory(self, idealFlightHeight, bombingEndPosition, bombingDir, bombingEndTime):
        ...
    def __generateRetreatPoints(self, bombingEndPosition, bombingEndTime, positions):
        ...
