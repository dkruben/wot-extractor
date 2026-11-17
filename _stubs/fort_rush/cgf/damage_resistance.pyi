# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/cgf/damage_resistance.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
from VehicleExpirableComponent import VehicleExpirableComponent as VehicleExpirableComponent
from constants import IS_EDITOR as IS_EDITOR
from debug_utils import LOG_WARNING as LOG_WARNING
from fort_rush_common.cgf import getTopMostGO as getTopMostGO
from FortRushDamageResistanceComponent import FortRushDamageResistanceComponent as FortRushDamageResistanceComponent
from helpers import dependency as dependency

class Vehicle(object):
    id: Any
    def __init__(self):
        ...

class battle_constants(object):
    class DestroyTimerViewState(object):
        def __init__(self, *args, **kwargs):
            ...
    class TIMER_VIEW_STATE(object):
        CRITICAL = 'critical'
        WARNING = 'warning'

class fort_rush_battle_constants(object):
    class FR_VEHICLE_VIEW_STATE(object):
        INVULNERABLE = 19807040628566084398385987584

class IBattleSessionProvider(object):
    def invalidateVehicleState(self, *args):
        ...

class BATTLE_CTRL_ID(object):
    FORT_RUSH_GUI_CTRL = None

class FortRushDamageResistanceSystem(CGF.System):
    DmgResistanceActivated: Any
    DmgResistanceRemoved: Any
    VehicleAccess: Any
    Reactions: Any
    __vehicleIDsByGameObject: Any
    def __init__(self):
        ...
    def onMappingUnloaded(self):
        ...
    def update(self):
        ...
    def onActivated(self, go, vehExpirebleCmp, vehicleAccess):
        ...
    def onRemoved(self, go, vehicleAccess):
        ...

def _getPlayerVehicleID(playerAvatar=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _notifyMarkerInvulnerability(vehicleID, isActive, guiSessionProvider=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _hideStatusEffect(vehicle, status, guiSessionProvider=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _showStatusEffect(vehicle, duration, status, level, guiSessionProvider=None):
    ...
