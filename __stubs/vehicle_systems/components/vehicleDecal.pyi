# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/vehicleDecal.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from vehicle_systems.tankStructure import TankPartNames as TankPartNames

class VehicleDecal(object):
    settingsCore: Any
    DECALS_OFF = 0
    OCCLUSION_DECAL = 1
    __attached: Any
    __appearance: Any
    __chassisDecals: Any
    __chassisParent: Any
    __hullDecals: Any
    __hullParent: Any
    __turretDecals: Any
    __turretParent: Any
    @staticmethod
    def getDecalType():
        ...
    def __init__(self, appearance):
        ...
    def destroy(self):
        ...
    def create(self):
        ...
    def attach(self):
        ...
    def detach(self):
        ...
    def __reattach(self, decalType):
        ...
    def onSettingsChanged(self, diff=None):
        ...
    def __createDecals(self, decalType):
        ...
    def __attach(self):
        ...
    def __createDecal(self, transform, applyToAll):
        ...
