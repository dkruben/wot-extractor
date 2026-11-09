# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/parts/guns/twin_shoot/custom_integrations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from events_handler import eventHandler as eventHandler
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle, ifObservedVehicle as ifObservedVehicle
from vehicles.parts.guns.common import GunShootingCustomIntegrations as GunShootingCustomIntegrations
from vehicles.parts.guns.twin_shoot.guns_interfaces import ITwinShootingListenerLogic as ITwinShootingListenerLogic
from Vehicular import DetailedGunState as DetailedGunState
_logger: Any

class TwinShootCustomIntegrations(GunShootingCustomIntegrations, ITwinShootingListenerLogic):
    @property
    def detailedGunState(self):
        ...
    # decorador original: @eventHandler
    def onAppearanceReady(self):
        ...
    # decorador original: @eventHandler
    def onActiveGunsUpdate(self, gunIndexes):
        ...
    # decorador original: @eventHandler
    def onAnimatedGunsUpdate(self, gunIndexes):
        ...
    # decorador original: @ifPlayerVehicle
    def _processAvatarSingleDiscreteShot(self, player=None):
        ...
    # decorador original: @ifObservedVehicle
    def __processAvatarActiveGunsUpdate(self, player=None, __=None, gunIndexes=...):
        ...
