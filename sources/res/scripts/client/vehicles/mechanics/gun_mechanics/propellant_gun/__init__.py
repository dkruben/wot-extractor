# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/__init__.py
from __future__ import absolute_import
import typing
from constants import PROPELLANT_GUN_STATE, SERVER_TICK_LENGTH
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_interfaces import IPropellantGunComponentParams, IPropellantGunMechanicState
from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_models import PropellantGunComponentParams, PropellantGunMechanicState
from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_events import PropellantStatesEvents
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_states import IMechanicStatesComponent
__all__ = ('IPropellantGunComponentParams', 'IPropellantGunMechanicState', 'PropellantGunComponentParams',
           'PropellantGunMechanicState', 'PropellantStatesEvents', 'DEFAULT_PROPELLANT_GUN_PARAMS',
           'DEFAULT_PROPELLANT_GUN_MECHANIC_STATE', 'createPropellantStatesEvents')
DEFAULT_PROPELLANT_GUN_PARAMS = PropellantGunComponentParams(10.0, 10.0, 100.0, 200.0, [], set())
DEFAULT_PROPELLANT_GUN_MECHANIC_STATE = PropellantGunMechanicState(state=PROPELLANT_GUN_STATE.IDLE, stageID=0, chargeProgress=0.0, isOvercharge=False, isSwitchCooldownActive=False, updateTime=0.0, isForbiddenShell=False, lastShotTimestamp=0.0, lastShotCharge=0.0, params=DEFAULT_PROPELLANT_GUN_PARAMS)

@activateEventsContainer()
def createPropellantStatesEvents(component, tickInterval=SERVER_TICK_LENGTH, **_):
    return PropellantStatesEvents(component, tickInterval)
