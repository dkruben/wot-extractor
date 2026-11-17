# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SecondaryGunComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.parts.guns.common import IGunComponent as IGunComponent, createGunShootingEvents as createGunShootingEvents
from vehicles.parts.guns.common import IGunShootingEvents as IGunShootingEvents

# decorador original: @ReprInjector.withParent(...)
class SecondaryGunComponent(VehicleDynamicComponent, IGunComponent):
    __shootingEvents: Any
    def __init__(self):
        ...
    @property
    def shootingEvents(self):
        ...
    def getGunInstallationIndex(self):
        ...
    def onDestroy(self):
        ...
    def onDiscreteShot(self, gunIndex):
        ...
    def onMultiShot(self, gunIndexes):
        ...
    def _onAppearanceReady(self):
        ...
    def _onAppearanceReset(self):
        ...
