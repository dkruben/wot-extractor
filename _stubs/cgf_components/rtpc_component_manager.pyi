# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/rtpc_component_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
from constants import IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from Sound import RTPCComponent as RTPCComponent, RTPCSourceType as RTPCSourceType
from Vehicular import RemainingAmmoClipPercentGetter as RemainingAmmoClipPercentGetter
from cgf_common.cgf_helpers import getVehicleEntityByVehicleGameObject as getVehicleEntityByVehicleGameObject

class Vehicle(object):
    ...

class RTPCComponentSystem(CGF.System):
    __sessionProvider: Any
    RTCPActivated: Any
    RTCPDeactivated: Any
    RTCPIterate: Any
    VehicleAccess: Any
    Reactions: Any
    __rtpcGameObjectToVehicleGameObject: Any
    def update(self):
        ...
    def __init__(self):
        ...
    def onMappingUnloaded(self):
        ...
    def getVehicleComponentForRTPC(self, rtpcGameObject):
        ...
