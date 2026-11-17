# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/CommandMapping.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import typing as typing
import BigWorld as BigWorld
import Input as Input
import logging as logging
import ResMgr as ResMgr
import Keys as Keys
import Event as Event
import Settings as Settings
from shared_utils import findFirst as findFirst
from debug_utils import LOG_DEBUG as LOG_DEBUG
from ResMgr import DataSection as DataSection
_logger: Any
g_instance = None
CMD_MOVE_FORWARD = 1
CMD_MOVE_FORWARD_SPEC = 2
CMD_MOVE_BACKWARD = 3
CMD_ROTATE_LEFT = 4
CMD_ROTATE_RIGHT = 5
CMD_INCREMENT_CRUISE_MODE = 6
CMD_DECREMENT_CRUISE_MODE = 7
CMD_STOP_UNTIL_FIRE = 8
CMD_SWITCH_SERVER_MARKER = 9
CMD_AMMO_CHOICE_1 = 10
CMD_AMMO_CHOICE_2 = 11
CMD_AMMO_CHOICE_3 = 12
CMD_AMMO_CHOICE_4 = 13
CMD_AMMO_CHOICE_5 = 14
CMD_AMMO_CHOICE_6 = 15
CMD_AMMO_CHOICE_7 = 16
CMD_AMMO_CHOICE_8 = 17
CMD_AMMO_CHOICE_9 = 18
CMD_AMMO_CHOICE_0 = 19
CMD_CHAT_SHORTCUT_BACKTOBASE = 22
CMD_CHAT_SHORTCUT_NEGATIVE = 25
CMD_CHAT_SHORTCUT_HELPME = 26
CMD_CM_SHOOT = 27
CMD_CM_SWITCH_TRAJECTORY = 28
CMD_CM_FREE_CAMERA = 29
CMD_CM_LOCK_TARGET = 30
CMD_CM_LOCK_TARGET_OFF = 31
CMD_CM_CAMERA_ROTATE_LEFT = 32
CMD_CM_CAMERA_ROTATE_RIGHT = 33
CMD_CM_CAMERA_ROTATE_UP = 34
CMD_CM_CAMERA_ROTATE_DOWN = 35
CMD_CM_VEHICLE_SWITCH_AUTOROTATION = 36
CMD_CM_INCREASE_ZOOM = 37
CMD_CM_DECREASE_ZOOM = 38
CMD_CM_ALTERNATE_MODE = 39
CMD_CM_CAMERA_RESTORE_DEFAULT = 40
CMD_CM_POSTMORTEM_NEXT_VEHICLE = 41
CMD_CM_POSTMORTEM_SELF_VEHICLE = 42
CMD_VEHICLE_MARKERS_SHOW_INFO = 43
CMD_AMMO_PANEL_SELECT = 44
CMD_MINIMAP_HIGHLIGHT_CELL = 45
CMD_MINIMAP_VEHICLE_SPECIFIC = 46
CMD_MINIMAP_SIZE_UP = 47
CMD_MINIMAP_SIZE_DOWN = 48
CMD_MINIMAP_VISIBLE = 49
CMD_VOICECHAT_MUTE = 50
CMD_TOGGLE_GUI = 53
CMD_RELOAD_PARTIAL_CLIP = 54
CMD_RADIAL_MENU_SHOW = 55
CMD_CHAT_SHORTCUT_RELOAD = 56
CMD_VOICECHAT_ENABLE = 57
CMD_BLOCK_TRACKS = 58
CMD_CM_TRAJECTORY_VIEW = 59
EPIC_GLOBAL_MSG_SAVE_TANKS = 60
EPIC_GLOBAL_MSG_TIME = 61
EPIC_GLOBAL_MSG_LEFT_LANE = 62
EPIC_GLOBAL_MSG_CENTER_LANE = 63
EPIC_GLOBAL_MSG_RIGHT_LANE = 64
EPIC_GLOBAL_MSG_FOCUS_HQ = 65
CMD_REQUEST_RECOVERY = 66
CMD_QUEST_PROGRESS_SHOW = 67
CMD_SHOW_HELP = 68
CMD_CM_CHARGE_SHOT = 69
CO_DEPENDENT_KEYS: dict
CMD_CHAT_SHORTCUT_CONTEXT_COMMAND = 70
CMD_CHAT_SHORTCUT_CONTEXT_COMMIT = 71
CMD_CHAT_SHORTCUT_THANKYOU = 72
CMD_CM_VEHICLE_UPGRADE_PANEL_LEFT = 73
CMD_CM_VEHICLE_UPGRADE_PANEL_RIGHT = 74
CMD_CM_VEHICLE_UPGRADE_PANEL_ALTERNATIVE_LEFT = 75
CMD_CM_VEHICLE_UPGRADE_PANEL_ALTERNATIVE_RIGHT = 76
CMD_UPGRADE_PANEL_SHOW = 77
CMD_CM_VEHICLE_ACTIVATE_RADAR = 78
CMD_CHAT_SHORTCUT_AFFIRMATIVE = 79
CMD_COMMANDER_CAM = 80
CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_1 = 81
CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_2 = 82
CMD_SHOW_PERSONAL_RESERVES = 83
CMD_CM_POSTMORTEM_TARGET_VEHICLE = 84
CMD_CM_POSTMORTEM_PREV_VEHICLE = 85
CMD_CM_FREE_CAMERA_PREV_VEHICLE = 86
CMD_TOGGLE_ARMOR_FLASHLIGHT = 87
CMD_CM_SPECIAL_ABILITY = 88

class CommandMapping(object):
    __DEFAULT_CONFIG_FILE_NAME = 'scripts/command_mapping.xml'
    __USER_CONFIG_SECTION_NAME = 'commandMapping'
    onMappingChanged: Any
    __mapping: Any
    __dictCommand2CommandName: Any
    def __init__(self):
        ...
    def add(self, commandName, fireKeyName, satelliteKeyNames=None, isDefault=False):
        ...
    def get(self, commandName):
        ...
    def getCommandKeys(self, command):
        ...
    def remove(self, commandName, fireKeyName=None, satelliteKeyNames=None, isDefault=None):
        ...
    def clear(self):
        ...
    def restoreDefault(self):
        ...
    def restoreUserConfig(self):
        ...
    def isActive(self, command):
        ...
    def isActiveList(self, listCommands, bAndNor=False):
        ...
    def isFired(self, command, key):
        ...
    def isFiredList(self, listCommands, key, bAndNor=False):
        ...
    def getName(self, command):
        ...
    def getCommand(self, name):
        ...
    def _setCommand(self, name, command):
        ...
    def _removeCommand(self, name):
        ...
    def save(self):
        ...
    def __checkUserKey(self, key):
        ...
    def __loadFromSection(self, section, bDelOldCmds=True, asDefault=False):
        ...
    def getDefaults(self):
        ...
    def __loadDefault(self):
        ...
    def __loadUserConfig(self):
        ...
    def __loadDevelopment(self):
        ...
