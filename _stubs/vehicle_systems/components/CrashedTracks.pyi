# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/CrashedTracks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from future.utils import lrange as lrange
import BigWorld as BigWorld
import Math as Math
import math_utils as math_utils
import CGF as CGF
import Vehicular as Vehicular
from cgf_script.registration import registerComponent as registerComponent
from items.components.component_constants import MAIN_TRACK_PAIR_IDX as MAIN_TRACK_PAIR_IDX, DEFAULT_TRACK_HIT_VECTOR as DEFAULT_TRACK_HIT_VECTOR, TrackState as TrackState
from items.vehicle_items import CHASSIS_ITEM_TYPE as CHASSIS_ITEM_TYPE
from vehicle_systems import model_assembler as model_assembler
from vehicle_systems.tankStructure import getPartModelsFromDesc as getPartModelsFromDesc, TankPartNames as TankPartNames, ModelsSetParams as ModelsSetParams
from vehicle_systems.stricted_loading import loadingPriority as loadingPriority, makeCallbackWeak as makeCallbackWeak
from constants import IS_EDITOR as IS_EDITOR

class _TRACK_SIDE(object):
    LEFT = 'left'
    RIGHT = 'right'

# decorador original: @registerComponent
class CrashedTracksController(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    __vehicleDesc: Any
    __entity: Any
    __modelsSet: Any
    __baseTrackFashion: Any
    __crashedTracks: Any
    __model: Any
    __fashion: Any
    __loading: Any
    __isActive: Any
    __visibilityMask: Any
    __tracksGo: Any
    __dynAccess: Any
    def __init__(self, vehicleDesc, trackFashion, modelsSet, tracksGo):
        ...
    def isLeftTrackBroken(self):
        ...
    def isRightTrackBroken(self):
        ...
    def hasDebris(self, isLeft, pairIndex):
        ...
    def getTrackStates(self, isLeft):
        ...
    def getPairsCnt(self):
        ...
    def setVehicle(self, entity):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def setVisible(self, visibilityMask):
        ...
    def receiveShotImpulse(self, direction, impulse):
        ...
    def addCrashedTrack(self, isLeft, pairIndex, hitPoint=None, isFlying=False, isDebris=False):
        ...
    def delCrashedTrack(self, isLeft, pairIndex):
        ...
    def __setupTrackAssembler(self, entity):
        ...
    def __hasCrashedTracks(self):
        ...
    def __setCrashedTrack(self, isLeft, pairIndex, isBroken, hitPoint, isDebris):
        ...
    def __loadModel(self, trackAssembler):
        ...
    def __getEmptyTrackStates(self, pairsCount):
        ...
    def __resetBrokenTracks(self):
        ...
    def __reset(self):
        ...
    def __isBrokenButDebris(self, side, index):
        ...
    def __setupTracksHiding(self):
        ...
    def __applyVisibilityMask(self):
        ...
    def __onModelLoaded(self, resources):
        ...

class CrashedTracksSystem(CGF.System):
    Activate: Any
    Deactivate: Any
    Reactions: Any
    def update(self):
        ...
