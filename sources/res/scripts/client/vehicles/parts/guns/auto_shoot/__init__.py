# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/parts/guns/auto_shoot/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/parts/guns/auto_shoot/__init__.py
from __future__ import absolute_import
import typing
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.parts.guns.auto_shoot.custom_integrations import AutoShootCustomIntegrations
from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootDispersionState, IAutoShootGunComponentState, IAutoShootGunComponent, IAutoShootingEvents, IAutoShootingListener
from vehicles.parts.guns.auto_shoot.shooting_events import AutoShootingEvents
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle
__all__ = ('IAutoShootDispersionState', 'IAutoShootGunComponentState', 'IAutoShootGunComponent',
           'IAutoShootingEvents', 'IAutoShootingListener', 'createAutoShootingEvents')

@activateEventsContainer()
def createAutoShootingEvents(vehicle, component, **_):
    shootingEvents = AutoShootingEvents(component)
    AutoShootCustomIntegrations(vehicle, component).subscribeTo(shootingEvents)
    return shootingEvents
