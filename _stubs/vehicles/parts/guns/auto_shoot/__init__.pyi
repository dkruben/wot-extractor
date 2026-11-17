# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/auto_shoot/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.container_wrappers import activateEventsContainer as activateEventsContainer
from vehicles.parts.guns.auto_shoot.custom_integrations import AutoShootCustomIntegrations as AutoShootCustomIntegrations
from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootDispersionState as IAutoShootDispersionState, IAutoShootGunComponentState as IAutoShootGunComponentState, IAutoShootGunComponent as IAutoShootGunComponent, IAutoShootingEvents as IAutoShootingEvents, IAutoShootingListener as IAutoShootingListener
from vehicles.parts.guns.auto_shoot.shooting_events import AutoShootingEvents as AutoShootingEvents
from Vehicle import Vehicle as Vehicle
__all__: tuple

# decorador original: @activateEventsContainer(...)
def createAutoShootingEvents(vehicle, component, **_):
    ...
