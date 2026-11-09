# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/vo_converters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.lobby.cyberSport import PLAYER_GUI_STATUS as PLAYER_GUI_STATUS
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeSlotsVOs as makeSlotsVOs, MAX_PLAYER_COUNT_ALL as MAX_PLAYER_COUNT_ALL, makeTotalLevelLabel as makeTotalLevelLabel, makeUnitStateLabel as makeUnitStateLabel, makeVehicleVO as makeVehicleVO
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.clans.stronghold_event_requester import FrozenVehiclesConstants as FrozenVehiclesConstants
from gui.prb_control import settings as settings
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from helpers import i18n as i18n
from shared_utils import BitmaskHelper as BitmaskHelper

class FILTER_STATE(BitmaskHelper):
    ALL = 0
    LIGHT_TANK = 1
    MEDIUM_TANK = 2
    HEAVY_TANK = 4
    SPG = 8
    AT_SPG = 16
    VEHICLE_TYPES: tuple

def _convertVehClassNamesToState(vehClassNames):
    ...
def makeStrongholdsSlotsVOs(unitEntity, unitMgrID=None, maxPlayerCount=...):
    ...
def makeSortieVO(unitEntity, isCommander, unitMgrID=None, canInvite=True, maxPlayerCount=...):
    ...
def disableCanBeTakenButtonInSlots(slots):
    ...
def setFreezedInSlots(slots):
    ...
def makeStrongholdVehicleVO(vehicle, levelsRange=None, vehicleTypes=None, isCurrentPlayer=True, frozenVehicles=None):
    ...
def _updateStrongholdEventVehicleVO(vehicleVO, frozenVehicles):
    ...
