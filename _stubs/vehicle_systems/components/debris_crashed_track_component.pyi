# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/debris_crashed_track_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
from cgf_script.registration import registerComponent as registerComponent
_logger: Any

# decorador original: @registerComponent
class DebrisCrashedTrackComponent(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    MAX_DEBRIS_COUNT: tuple
    CURRENT_DEBRIS_COUNT = 0
    isLeft: Any
    pairIndex: Any
    vehicleDescriptor: Any
    wheelsGameObject: Any
    boundEffects: Any
    vehicleFilter: Any
    debrisGameObject: Any
    trackPairDesc: Any
    __isLeft: Any
    __pairIndex: Any
    __vehicleDescriptor: Any
    __wheelsGameObject: Any
    __boundEffects: Any
    __vehicleFilter: Any
    __isPlayer: Any
    __shouldCreateDebris: Any
    __hitPoint: Any
    __modelsSet: Any
    __debrisGameObject: Any
    @property
    def debrisDesc(self):
        ...
    @property
    def hitPoint(self):
        ...
    @property
    def shouldCreateDebris(self):
        ...
    @property
    def isPlayer(self):
        ...
    @property
    def modelsSet(self):
        ...
    def __init__(self, isLeft, pairIndex, vehicleDescriptor, wheelsGameObject, boundEffects, vehicleFilter, isPlayerVehicle, shouldCreateDebris, hitPoint, modelsSet='default'):
        ...
    def createDebrisGameObject(self, queue):
        ...
    def removeDebrisGameObject(self):
        ...

class NodeRemapperComponent(object):
    nodes: Any
    __nodes: Any
    def __init__(self, nodes):
        ...
