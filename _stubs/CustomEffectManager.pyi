# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/CustomEffectManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
import BigWorld as BigWorld
import Math as Math
import CGF as CGF
import material_kinds as material_kinds
from constants import IS_EDITOR as IS_EDITOR
from helpers.PixieNode import PixieCache as PixieCache
from CustomEffect import EffectSettings as EffectSettings
from vehicle_systems.tankStructure import TankNodeNames as TankNodeNames
from cgf_script.registration import registerComponent as registerComponent
import Vehicular as Vehicular
from items.vehicles import VehicleDescriptor as VehicleDescriptor
_ENABLE_VALUE_TRACKER = False
_ENABLE_VALUE_TRACKER_ENGINE = False
_ENABLE_PIXIE_TRACKER = False
_VEHICLE_DIRECTION_THRESHOLD = 0.1

# decorador original: @registerComponent
class CustomEffectManager(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    _LEFT_TRACK = 0
    _RIGHT_TRACK = 1
    _DRAW_ORDER_IDX = 50
    __selectors: Any
    __variableArgs: Any
    __vehicle: Any
    __appearance: Any
    __prevWaterHeight: Any
    __gearUP: Any
    __trailParticleNodes: Any
    __hullSelectors: Any
    __chassisSelectors: Any
    __wheelsData: Any
    __selectorsEnabled: Any
    __effectsToReset: Any
    __vt: Any
    @property
    def variables(self):
        ...
    def __init__(self, appearance):
        ...
    def disableDefaultSelectors(self, disableChassis, disableHull):
        ...
    def setWheelsData(self, typeDescriptor, wheelsAnimator):
        ...
    def getParameter(self, name):
        ...
    def destroy(self):
        ...
    def enable(self, enable, settingsFlags=...):
        ...
    def setVehicle(self, vehicle):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def enableSelectors(self):
        ...
    def disableSelectors(self):
        ...
    def __createChassisCenterNodes(self):
        ...
    def onGearUp(self):
        ...
    def scheduleResetForEffect(self, varName):
        ...
    def update(self, wheelsAnimator, engineState, waterSensor):
        ...
    @staticmethod
    def __getScrollParams(trackScrolldelta, hasContact, matKindsUnderTrack, direction):
        ...
    def __correctWaterNodes(self, waterSensor):
        ...
    def remapNode(self, fromNode, toNode=''):
        ...

class CustomEffectManagerSystem(CGF.System):
    Activate: Any
    Deactivate: Any
    Reactions: Any
    def update(self):
        ...

def getCorrectedMatKinds(terrainMatKind, waterSensor):
    ...
def isVehicleAttached(vehicle):
    ...
