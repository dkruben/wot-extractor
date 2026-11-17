# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/common/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.container_wrappers import activateEventsContainer as activateEventsContainer
from vehicles.parts.guns.common.custom_integrations import GunShootingCustomIntegrations as GunShootingCustomIntegrations
from vehicles.parts.guns.common.guns_interfaces import IGunComponent as IGunComponent, IGunShootingEvents as IGunShootingEvents, IGunShootingEventsLogic as IGunShootingEventsLogic, IGunShootingListener as IGunShootingListener, IGunShootingListenerLogic as IGunShootingListenerLogic
from vehicles.parts.guns.common.shooting_events import GunShootingEvents as GunShootingEvents, GunShootingCoreIntegration as GunShootingCoreIntegration, GunShootingEventsDebugger as GunShootingEventsDebugger
from Vehicle import Vehicle as Vehicle
__all__: tuple

# decorador original: @activateEventsContainer(...)
def createGunShootingEvents(vehicle, component, **_):
    ...
