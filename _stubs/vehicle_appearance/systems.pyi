# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/vehicle_appearance/systems.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
import Vehicular as Vehicular
from CustomEffectManager import CustomEffectManager as CustomEffectManager
from vehicle_appearance.common_tank_appearance import ActivateContext as ActivateContext, DeactivateContext as DeactivateContext, UpdateContext as UpdateContext, DestroyContext as DestroyContext
from vehicle_appearance import constants as appearance_constants
from vehicle_systems.CompoundAppearance import UpdateDirtContext as UpdateDirtContext
from vehicle_systems.components.CrashedTracks import CrashedTracksController as CrashedTracksController
from vehicle_systems.components.highlighter import Highlighter as Highlighter
from vehicle_systems.components.hull_aiming_controller import HullAimingController as HullAimingController
from vehicle_systems.components.vehicle_shadow_manager import VehicleShadowManager as VehicleShadowManager
from vehicle_systems.components.siegeEffectsController import SiegeEffectsController as SiegeEffectsController
from vehicle_appearance.component import VehicleAppearanceComponent as VehicleAppearanceComponent
from vehicle_appearance.common_tank_appearance import CommonTankAppearance as CommonTankAppearance
_logger: Any

class CommonTankAppearanceActivateSystem(CGF.System):
    Create: Any
    Activate: Any
    Deactivate: Any
    Remove: Any
    Reactions: Any
    def update(self):
        ...
    def __deactivateAppearance(self, reactions):
        ...
    def __destroyAppearance(self, reactions):
        ...
    def __activateAppearance(self, reactions):
        ...

class CommonTankAppearanceUpdateSystem(CGF.System):
    UpdateIterate: Any
    Reactions: Any
    def update(self):
        ...

class CompoundAppearanceDirtUpdateSystem(CGF.System):
    UpdateIterate: Any
    Reactions: Any
    def update(self):
        ...
