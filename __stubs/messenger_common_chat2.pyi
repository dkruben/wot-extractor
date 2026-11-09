# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/messenger_common_chat2.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from string import Template as Template
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, CHAT_COMMANDS_THAT_IGNORE_COOLDOWNS as CHAT_COMMANDS_THAT_IGNORE_COOLDOWNS, GENERIC_MESSENGER_ARGS as GENERIC_MESSENGER_ARGS
from constants import IS_CLIENT as IS_CLIENT, IS_CHINA as IS_CHINA
from math_common import decimal_round as decimal_round
_g_id = None
_COOLDOWN_OFFSET: Any
_INITIAL_DEFAULT_BATTLE_CHAT_COOLDOWN_DURATION = 0.1
_SHORT_BATTLE_CHAT_COOLDOWN_DURATION = 0.0
_TEAM_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 6.0
_SAME_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 5.0
_SAME_PRIVATE_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 2.0
_OTHER_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 1.0
_ATTENTION_TO_COMMAND_COOLDOWN_DURATION = 0.2
_SAME_TARGET_PERSONAL_BATTLE_CHAT_CMD_COOLDOWN_DURATION = 3.0
_REACTIONAL_CHAT_CMD_COOLDOWN_DURATION = 0.1
_MAX_ATTENTION_TO_CHAT_COMMANDS_WITHIN_TIMEFRAME = 3
_TIMEFRAME_FOR_ATTENTION_TO_STORAGE = 5
_MAX_ATTENTION_TO_PER_TEAM = 3
EMPTY_ARGS: Any
VOIP_CREDS_MODE_DEFAULT = 0
VOIP_CREDS_MODE_CHANNEL_REFRESH = 1
RESPONSE_MESSENGER_ACTION_IDS: tuple
_MESSENGER_ACTION_NAMES: dict
_MESSENGER_ERROR_NAMES: dict
AdminChatCommand: Any
ADMIN_CHAT_COMMANDS: tuple
ADMIN_CHAT_COMMANDS_BY_NAMES: dict
BattleChatCommand: Any
UnitChatCommand: Any
UNIT_CHAT_COMMANDS: tuple
UNIT_CHAT_COMMANDS_BY_NAMES: dict
BATTLE_CHAT_COMMANDS: list
BATTLE_CHAT_COMMANDS_BY_NAMES: dict
ExtBattleChatCommand: Any
MUC_SERVICE_TYPES: Any
ChatCommandBlockedData: Any
COOLDOWN_SETTING_NAMES: tuple
BattleChatCmdGameModeCoolDownData: Any
DEFAULT_SPAM_PROTECTION_SETTING: Any
BATTLE_CMD_COOLDOWN_ALLOWED_MARGIN = 0.1

class MESSENGER_ERRORS:
    NO_ERROR: Any
    GENERIC_ERROR: Any
    NOT_READY: Any
    IN_COOLDOWN: Any
    COMMAND_IN_TEAM_COOLDOWN: Any
    IN_CHAT_BAN: Any
    IS_BUSY: Any
    NOT_ALLOWED: Any
    WRONG_ARGS: Any
    USER_NOT_FOUND: Any
    CANNOT_BAN_ONESELF: Any
    CUSTOM_ERROR_ID: Any
    @staticmethod
    def getErrorName(errorCode):
        ...

class MESSENGER_LIMITS:
    FIND_USERS_BY_NAME_MAX_RESULT_SIZE = 50
    FIND_USERS_BY_NAME_REQUEST_COOLDOWN_SEC: Any
    BATTLE_CHANNEL_MESSAGE_MAX_SIZE = 140
    UNIT_CHANNEL_MESSAGE_MAX_SIZE = 512
    BATTLE_CHAT_HISTORY_ON_SERVER_MAX_LEN = 10
    UNIT_CHAT_HISTORY_ON_SERVER_MAX_LEN = 20
    BROADCASTS_FROM_CLIENT_COOLDOWN_SEC: Any
    ADMIN_COMMANDS_FROM_CLIENT_COOLDOWN_SEC: Any
    VOIP_CREDENTIALS_REQUEST_COOLDOWN_SEC: Any

class MESSENGER_ACTION_IDS:
    RESPONSE_SUCCESS: Any
    RESPONSE_FAILURE: Any
    FIND_USERS_BY_NAME: Any
    GET_VOIP_CREDENTIALS: Any
    LOG_VIVOX_LOGIN: Any
    ENTER_VOIP_CHANNEL: Any
    LEAVE_VOIP_CHANNEL: Any
    _ADMIN_COMMAND_START_ID: Any
    _BATTLE_ACTION_START_ID: Any
    INIT_BATTLE_CHAT: Any
    REINIT_BATTLE_CHAT: Any
    DEINIT_BATTLE_CHAT: Any
    BROADCAST_BATTLE_MESSAGE: Any
    ON_BATTLE_MESSAGE_BROADCAST: Any
    _BATTLE_CHAT_COMMAND_START_ID: Any
    _BATTLE_ACTION_END_ID: Any
    _UNIT_ACTION_START_ID: Any
    INIT_UNIT_CHAT: Any
    DEINIT_UNIT_CHAT: Any
    BROADCAST_UNIT_MESSAGE: Any
    ON_UNIT_MESSAGE_BROADCAST: Any
    _UNIT_COMMAND_START_ID: Any
    _UNIT_ACTION_END_ID: Any
    CUSTOM_ACTION_ID: Any
    @staticmethod
    def getActionName(actionID):
        ...
    @staticmethod
    def isBattleChatAction(actionID):
        ...
    @staticmethod
    def isUnitChatAction(actionID):
        ...
    @staticmethod
    def isRateLimitedBroadcastFromClient(actionID):
        ...
    @staticmethod
    def isChatActionSusceptibleToBan(actionID):
        ...
    @staticmethod
    def battleChatCommandFromActionID(actionID):
        ...
    @staticmethod
    def unitChatCommandFromActionID(actionID):
        ...
    @staticmethod
    def adminChatCommandFromActionID(actionID):
        ...

class CHAT_COMMAND_COOLDOWN_TYPE_IDS:
    TIMEFRAME_DATA_COOLDOWN: Any
    SAME_COMMAND_COOLDOWN: Any
    OTHER_COMMANDS_COOLDOWN: Any
    PRIVATE_COMMANDS_COOLDOWN: Any
    ATTENTION_TO_BLOCKED_COOLDOWN: Any

class MUC_SERVICE_TYPE(object):
    STANDARD = 1
    USER = 2
    CLAN = 3

def _makeID(start=None, range=None):
    ...
def messageArgs(int32Arg1=0, int64Arg1=0, floatArg1=0, strArg1='', strArg2='', int8Arg1=0):
    ...
def addBattleChatCommand(extCommand):
    ...
def resolveMucRoomsOfService(service):
    ...
def canResolveMucRoomsOfService(service):
    ...
def areSenderCooldownsActive(currTime, listOfCoolDownTimeData, cmdIDToSend, targetIDToSend):
    ...
def addCoolDowns(currTime, listOfCoolDownTimeData, cmdID, cmdName, cmdCooldownTime, cmdTargetID, reqID, cooldownConf):
    ...
