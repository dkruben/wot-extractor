# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarPositionControl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import logging as logging
import math_utils as math_utils
import BigWorld as BigWorld
import Math as Math
from Event import Event as Event
import constants as constants
import BattleReplay as BattleReplay
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_logger: Any

class ConsistentMatrices(object):
    __attachedVehicleMatrix: Any
    __ownVehicleMProv: Any
    __ownVehicleTurretMProv: Any
    onVehicleMatrixBindingChanged: Any
    def __init__(self):
        ...
    @property
    def attachedVehicleMatrix(self):
        ...
    @property
    def ownVehicleMatrix(self):
        ...
    @property
    def ownVehicleTurretMProv(self):
        ...
    def notifyEnterWorld(self, avatar):
        ...
    def notifyLeaveWorld(self, avatar):
        ...
    def notifyVehicleLoaded(self, avatar, vehicle):
        ...
    def notifyPreBind(self, avatar):
        ...
    def notifyVehicleChanged(self, avatar, updateStopped=False):
        ...
    def notifyViewPointChanged(self, avatar, staticPosition=None):
        ...
    def __setTarget(self, matrix, asStatic=True):
        ...
    def __linkOwnVehicle(self, vehicle):
        ...

class AvatarPositionControl(CallbackDelayer):
    FOLLOW_CAMERA_MAX_DEVIATION = 7.0
    onAvatarVehicleChanged: Any
    isSwitching: Any
    __avatar: Any
    __bFollowCamera: Any
    __isSwitching: Any
    def __init__(self, avatar):
        ...
    def destroy(self):
        ...
    def bindToVehicle(self, bValue=True, vehicleID=None):
        ...
    def followCamera(self, bValue=True):
        ...
    def switchViewpoint(self, isViewpoint, vehOrPointId):
        ...
    def moveTo(self, pos):
        ...
    def getFollowCamera(self):
        ...
    def __resetSwitching(self):
        ...
    def __followCameraTick(self):
        ...
    def __doBind(self, vehicleID):
        ...
    def __doUnbind(self, vehicleID=None):
        ...
