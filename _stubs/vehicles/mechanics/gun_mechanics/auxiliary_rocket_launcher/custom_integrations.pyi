# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/custom_integrations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.armor_flashlight.utils import ArmorFlashlightHideReason as ArmorFlashlightHideReason
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from Avatar import PlayerAvatar as PlayerAvatar
from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher.mechanic_models import AuxiliaryRocketLauncherState as AuxiliaryRocketLauncherState

class AuxiliaryRocketLauncherCustomIntegrations(ContainersListener, IMechanicStatesListenerLogic):
    __sessionProvider: Any
    _component: Any
    def __init__(self, component):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onEventsContainerDestroy(self, events):
        ...
    def isPlayerVehicle(self, player):
        ...
    # decorador original: @ifPlayerVehicle
    def __updateArmorFlashlightVisibility(self, _, isInAimingMode):
        ...
