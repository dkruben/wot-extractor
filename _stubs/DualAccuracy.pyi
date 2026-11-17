# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/DualAccuracy.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from constants import DUAL_ACCURACY_STATE as DUAL_ACCURACY_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
_DEFAULT_ACCURACY_FACTOR = 1.0

# decorador original: @ReprInjector.withParent(...)
class DualAccuracy(VehicleDynamicComponent, IGunMechanicComponent):
    __dualAccuracyFactor: Any
    __eManager: Any
    onSetDualAccState: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    def isActive(self):
        ...
    def getComponentParams(self):
        ...
    def getCurrentDualAccuracyFactor(self):
        ...
    def getDualAccuracyFactor(self):
        ...
    def set_state(self, _=None):
        ...
    def onDestroy(self):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
