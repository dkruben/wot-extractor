# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/ModelHitTester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from Math import Vector2 as Vector2, Matrix as Matrix
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT, IS_CLIENT as IS_CLIENT, IS_BOT as IS_BOT
from debug_utils import LOG_DEBUG as LOG_DEBUG
from soft_exception import SoftException as SoftException
from constants import IS_EDITOR as IS_EDITOR
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
from items import _xml as _xml
from py2to3.patched_future import with_metaclass as with_metaclass
_logger: Any
SegmentCollisionResult: Any

class ModelStatus:
    NORMAL = 0
    CRASHED = 1

# base nao representavel no stub: with_metaclass(...)
class HitTesterManager:
    NORMAL_MODEL_TAG = 'normal'
    CRASHED_MODEL_TAG = 'crashed'
    CLIENT_MODEL_TAG = 'collisionModelClient'
    SERVER_MODEL_TAG = 'collisionModelServer'
    CLIENT_CAPSULE_TAG = 'capsuleScale'
    __hitTesters: Any
    __status: Any
    def __init__(self, dataSection=None):
        ...
    @property
    def modelHitTester(self):
        ...
    @modelHitTester.setter
    def modelHitTester(self, hitTester):
        ...
    @property
    def crashedModelHitTester(self):
        ...
    @crashedModelHitTester.setter
    def crashedModelHitTester(self, hitTester):
        ...
    @property
    def activeHitTester(self):
        ...
    def initHitTesters(self, dataSection):
        ...
    def setStatus(self, modelStatus):
        ...
    def loadHitTesters(self):
        ...
    def save(self, section):
        ...
    def __createHitTester(self, section, modelTag=None):
        ...

class ModelHitTester(object):
    __slots__: tuple
    bbox: Any
    __bspModel: Any
    __bspModelName: Any
    __bspModelDown: Any
    __bspModelNameDown: Any
    __bspModelUp: Any
    __bspModelNameUp: Any
    __extraCapsuleScale: Any
    bboxDown: Any
    bboxUp: Any
    def __init__(self, bspModelName=None, bspModelNameDown=None, bspModelNameUp=None, extraCapsuleScale=None):
        ...
    @property
    def bspModelName(self):
        ...
    @bspModelName.setter
    def bspModelName(self, name):
        ...
    def getBspModel(self):
        ...
    def isBspModelLoaded(self):
        ...
    @property
    def extraCapsuleScale(self):
        ...
    def loadBspModel(self):
        ...
    def releaseBspModel(self):
        ...
    def localAnyHitTest(self, start, stop, value=0):
        ...
    def localHitTest(self, start, stop, value=0):
        ...
    def localNearestHitTest(self, start, stop, value=0):
        ...
    def localHitTestFull_debug(self, start, stop, value=0):
        ...
    def worldHitTest(self, start, stop, worldMatrix, value=0):
        ...
    def localSphericHitTest(self, center, radius, outsidePolygonsOnly=True, allCollisions=False, value=0):
        ...
    def localCollidesWithTriangle(self, triangle, hitDir, value=0):
        ...
    def __getBspModel(self, value):
        ...
    def getModel(self, value):
        ...

class BoundingBoxManager(object):
    __status: Any
    __bboxes: Any
    def __init__(self, normalBBox=None, crashedBBox=None):
        ...
    def setStatus(self, modelStatus):
        ...
    @property
    def normalBBox(self):
        ...
    @normalBBox.setter
    def normalBBox(self, bbox):
        ...
    @property
    def crashedBBox(self):
        ...
    @crashedBBox.setter
    def crashedBBox(self, bbox):
        ...
    @property
    def activeBBox(self):
        ...
    @activeBBox.setter
    def activeBBox(self, bbox):
        ...

def segmentMayHitVolume(boundingRadius, center, segmentStart, segmentEnd):
    ...
def coneMayHitVolume(boundingRadius, center, segmentStart, segmentEnd, startDeviation, endDeviation, do2DTest=True):
    ...
def segmentMayHitVehicle(vehicleDescr, segmentStart, segmentEnd, vehicleCenter):
    ...
def combineBBoxes(bboxes):
    ...
def createBBoxManagerForModels(hitTesterManagers):
    ...
