# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/arena_info/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
from gui.shared.gui_items.Vehicle import VEHICLE_BATTLE_TYPES_ORDER_INDICES as VEHICLE_BATTLE_TYPES_ORDER_INDICES
from shared_utils import BitmaskHelper as BitmaskHelper
__all__: tuple
CONTOUR_ICON_SF_PATH = '../maps/icons/vehicle/contour/{0}.png'
CONTOUR_ICON_RES_PATH = 'gui/maps/icons/vehicle/contour/{0}.png'
DEFAULT_SCREEN_MAP_IMAGE_RES_PATH = 'gui/maps/icons/map/screen/default_screen.dds'
UNKNOWN_CONTOUR_ICON_NAME = 'unknown'
UNKNOWN_CONTOUR_ICON_SF_PATH: Any
UNKNOWN_CONTOUR_ICON_RES_PATH: Any
UNKNOWN_VEHICLE_NAME = INGAME_GUI.PLAYERS_PANEL_UNKNOWN_VEHICLE
UNKNOWN_VEHICLE_CLASS_NAME = 'unknown'
UNKNOWN_PLAYER_NAME = INGAME_GUI.PLAYERS_PANEL_UNKNOWN_NAME
UNKNOWN_VEHICLE_LEVEL = -1
UNKNOWN_VEHICLE_CLASS_ORDER = 100
SQUAD_RANGE_TO_SHOW: Any

class ARENA_LISTENER_SCOPE(object):
    LOAD = 1
    VEHICLES = 2
    TEAMS_BASES = 4
    PERIOD = 8
    INVITATIONS = 16
    POSITIONS = 32
    CONTACTS = 64
    VIEW_POINTS = 128
    OVERRIDE_SETTINGS = 256

class VEHICLE_STATUS(BitmaskHelper):
    DEFAULT = 0
    IS_ALIVE = 1
    IS_READY = 2
    NOT_AVAILABLE = 4
    STOP_RESPAWN = 8

class PLAYER_STATUS(BitmaskHelper):
    DEFAULT = 0
    IS_TEAM_KILLER = 1
    IS_SQUAD_MAN = 2
    IS_SQUAD_PERSONAL = 4
    IS_PLAYER_SELECTED = 8
    IS_VOIP_DISABLED = 16
    IS_ACTION_DISABLED = 32

class INVITATION_DELIVERY_STATUS(BitmaskHelper):
    NONE = 0
    FORBIDDEN_BY_RECEIVER = 1
    FORBIDDEN_BY_SENDER = 2
    RECEIVED_FROM = 4
    RECEIVED_INACTIVE = 8
    SENT_TO = 16
    SENT_INACTIVE = 32

class PERSONAL_STATUS(BitmaskHelper):
    DEFAULT = 0
    CAN_SEND_INVITE_TO_ALLY = 1
    CAN_SEND_INVITE_TO_ENEMY = 2
    SQUAD_RESTRICTIONS = 4
    IS_VEHICLE_LEVEL_SHOWN = 8
    IS_VEHICLE_COUNTER_SHOWN = 16
    IS_COLOR_BLIND = 32
    SHOW_ALLY_INVITES = 64
    SHOW_ENEMY_INVITES = 128

class INVALIDATE_OP(BitmaskHelper):
    NONE = 0
    SORTING = 1
    VEHICLE_STATUS = 2
    VEHICLE_INFO = 4
    VEHICLE_STATS = 8
    VEHICLE_ISTATS = 16
    PLAYER_STATUS = 32
    PREBATTLE_CHANGED = 64
    INVITATION_DELIVERY_STATUS = 128

class VehicleSpottedStatus(BitmaskHelper):
    DEFAULT = 0
    SPOTTED = 1
    UNSPOTTED = 2

def makeVehicleIconName(vName):
    ...
def makeContourIconSFPath(vName):
    ...
def makeContourIconResPath(vName):
    ...
def getOrderByVehicleClass(className=None):
    ...
