# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/common/guns_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer, IClientEventsContainerListener as IClientEventsContainerListener
from vehicles.components.component_interfaces import IVehicleGunSlotComponent as IVehicleGunSlotComponent

class IGunComponent(IVehicleGunSlotComponent):
    @property
    def shootingEvents(self):
        ...

class IGunShootingEventsLogic(object):
    onAppearanceReady = None
    onDiscreteShot = None
    onMultiShot = None
    def processAppearanceReady(self):
        ...
    def processAppearanceReset(self):
        ...
    def processDiscreteShot(self, gunIndex):
        ...
    def processMultiShot(self, gunIndexes):
        ...

class IGunShootingEvents(IClientEventsContainer, IGunShootingEventsLogic):
    ...

class IGunShootingListenerLogic(object):
    def onAppearanceReady(self):
        ...
    def onDiscreteShot(self, gunIndex):
        ...
    def onMultiShot(self, gunIndexes):
        ...

class IGunShootingListener(IClientEventsContainerListener, IGunShootingListenerLogic):
    ...
