# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/entities/vehicle_events/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer, IClientEventsContainerListener as IClientEventsContainerListener
from gui.battle_control.components_states.ammo import IComponentAmmoState as IComponentAmmoState
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot
from vehicles.entities import ShotParams as ShotParams

class IVehicleEventsLogic(object):
    onAppearanceReady = None
    onAppearanceReset = None
    onSiegeStateUpdated = None
    onVehicleDestroyed = None
    onObserverVehicleDataUpdated = None
    onCollectAmmoStates = None
    onCollectShotParams = None
    onCurrentShellChanged = None
    onDynamicComponentCreated = None
    onDynamicComponentDestroyed = None
    onDiscreteShotDone = None
    onShowDamageFromShot = None
    onVehicleHealthChanged = None
    def collectAmmoStates(self):
        ...

class IVehicleEvents(IClientEventsContainer, IVehicleEventsLogic):
    ...

class IVehicleEventsListenerLogic(object):
    def onAppearanceReady(self):
        ...
    def onAppearanceReset(self):
        ...
    def onSiegeStateUpdated(self, newState, timeToNextMode):
        ...
    def onVehicleDestroyed(self):
        ...
    def onObserverVehicleDataUpdated(self):
        ...
    def onCollectAmmoStates(self, ammoStates):
        ...
    def onCollectShotParams(self, shotParamsList):
        ...
    def onCurrentShellChanged(self, intCD):
        ...
    def onDynamicComponentCreated(self, component):
        ...
    def onDynamicComponentDestroyed(self, component):
        ...
    def onDiscreteShotDone(self, gunInstallationSlot):
        ...
    def onShowDamageFromShot(self, attackerID, hitPoints, effectsIndex, damageFactor, lastMaterialIsShield):
        ...
    def onVehicleHealthChanged(self, vehicleID, newHealth, oldHealth):
        ...

class IVehicleEventsListener(IClientEventsContainerListener, IVehicleEventsListenerLogic):
    ...
