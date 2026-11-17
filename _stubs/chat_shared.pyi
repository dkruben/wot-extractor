# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/chat_shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import zlib as zlib
from functools import wraps as wraps
from future.moves import pickle as pickle
from past.builtins import long as long, basestring as basestring
import constants as constants
from Event import Event as Event
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from constants import CHAT_LOG as CHAT_LOG, RESTRICTION_TYPE as RESTRICTION_TYPE
from debug_utils import LOG_ERROR as LOG_ERROR
from enumerations import Enumeration as Enumeration, AttributeEnumItem as AttributeEnumItem
from messenger_common_chat2 import BATTLE_CHAT_COMMANDS_BY_NAMES as BATTLE_CHAT_COMMANDS_BY_NAMES
from soft_exception import SoftException as SoftException
from wotdecorators import noexcept as noexcept
__all__: list
NOTIFICATION_GROUP: Any
CHAT_ACTIONS: Any
CHAT_RESPONSES: Any
__DEFAULT_COOLDOWN = 0.5
__BATTLE_COMMANDS_DEFAULT_COOLDOWN = __DEFAULT_COOLDOWN
__CHINA_USER_MESSAGE_COOLDOWN = 3.0
__COOLDOWN_CHECK_CLIENT = 1
__COOLDOWN_CHECK_BASE = 2
__COOLDOWN_CHECK_ALL: Any
CHAT_COMMANDS: Any
CHAT_MEMBER_STATUSES: Any
CHAT_MEMBER_BAN_TYPE: Any
CHAT_MEMBER_ROLE: Any
CHAT_MEMBER_GROUP: Any
CHAT_CHANNEL_BATTLE_TEAM = 1
CHAT_CHANNEL_BATTLE = 2
CHAT_CHANNEL_PREBATTLE = 4
CHAT_CHANNEL_PRIVATE = 8
CHAT_CHANNEL_DESTROYING = 16
CHAT_CHANNEL_TRAINING = 32
CHAT_CHANNEL_SQUAD = 64
CHAT_CHANNEL_TEAM = 128
CHAT_CHANNEL_VOICE = 256
CHAT_CHANNEL_CLAN = 512
CHAT_CHANNEL_PREBATTLE_CLAN = 1024
CHAT_CHANNEL_TOURNAMENT = 2048
CHAT_CHANNEL_UNIT = 4096
CHAT_CHANNEL_NOTIFY_MEMBERS_MASK = 3
CHAT_CHANNEL_NOTIFY_MEMBERS_IN_OUT = 0
CHAT_CHANNEL_NOT_NOTIFY_MEMBERS_IN_OUT = 1
CHAT_CHANNEL_NOTIFY_MEMBERS_COUNT = 2
CHAT_CHANNEL_NOTIFY_MEMBERS_DELTA = 3
ChatChannelKeyPrefix = 'chatChannel_'
_g_chatCommandProcessors: dict
g_chatCooldownData: Any
_g_chatadmins: list
SYS_MESSAGE_TYPE: Any
SYS_MESSAGE_IMPORTANCE: Any
SM_REQUEST_PERSONAL_MESSAGES_FLAG = 1
SM_REQUEST_SYSTEM_MESSAGES_FLAG = 2
SM_REQUEST_INTERNAL_SYS_MESSAGES_FLAG = 4
USERS_ROSTER_FRIEND = 1
USERS_ROSTER_IGNORED = 2
USERS_ROSTER_VOICE_MUTED = 4

class CHAT_STATUS:
    OK = 0
    NONE_OR_DESTROYED = 1
    ORIGIN_DISCONNECTED = 2

class BaseChatCommandProcessor(object):
    _command: Any
    __command: Any
    def __init__(self, comand):
        ...
    def parseRawData(self, rawData, verifyData=True):
        ...
    def verifyParsedData(self, int64Arg=0, int16arg=0, stringArg1='', stringArg2=''):
        ...
    def _verifyTupledData(self, dataAsTuple):
        ...
    def __verifyRawData(self, rawData):
        ...
    def _makeTuple(self, rawData):
        ...
    def _adjustTupleDataTypes(self, rawTuple):
        ...
    def set_command(self, newValue):
        ...

class OneStringArgCommandProcessor(BaseChatCommandProcessor):
    def __init__(self, command):
        ...
    def _makeTuple(self, rawData):
        ...

class NoArgsCommandProcessor(BaseChatCommandProcessor):
    def __init__(self, command):
        ...

class BanCommandProcessor(BaseChatCommandProcessor):
    def __init__(self):
        ...
    def _makeTuple(self, rawData):
        ...
    def verifyParsedData(self, int64Arg=0, int16arg=0, stringArg1='', stringArg2=''):
        ...

class UserCommandProcessor(BaseChatCommandProcessor):
    _USER_BAN_TYPES: Any
    def __init__(self, command):
        ...

class UserBanCommandProcessor(UserCommandProcessor):
    __BAN_TIME_RE: Any
    def __init__(self):
        ...
    def _makeTuple(self, rawData):
        ...
    def verifyParsedData(self, int64Arg=0, int16arg=0, stringArg1='', stringArg2=''):
        ...

class UserUnbanCommandProcessor(UserCommandProcessor):
    def __init__(self):
        ...
    def _makeTuple(self, rawData):
        ...
    def verifyParsedData(self, int64Arg=0, int16arg=0, stringArg1='', stringArg2=''):
        ...

class ChatActionHandlers(object):
    __actionHandlers: Any
    def __init__(self):
        ...
    def _onEntityInit(self):
        ...
    def _onEntityRestore(self):
        ...
    def _onEntityDestroy(self):
        ...
    def _clear(self):
        ...
    def _getActionHandlers(self, actionId):
        ...
    def _subscribeActionHandler(self, actionId, handler):
        ...
    def _unsubscribeActionHandler(self, actionId, handler):
        ...

class ChatError(SoftException):
    response: Any
    message: Any
    messageArgs: Any
    __response: Any
    __auxMessage: Any
    _messageArgs: Any
    def __init__(self, response=None, auxMessage=None, messageArgs=None):
        ...
    def _getMessage(self):
        ...
    def __get_message(self):
        ...

class UserBannedError(ChatError):
    __banOwnerNick: Any
    __banReason: Any
    __banEndTime: Any
    _messageArgs: Any
    def __init__(self, banOwnerNick, banReason, banEndTime):
        ...
    def _getMessage(self):
        ...

class ChatBannedError(ChatError):
    __banReason: Any
    __banEndTime: Any
    _messageArgs: Any
    def __init__(self, banReason, banEndTime):
        ...
    def _getMessage(self):
        ...

class ChatSQLError(ChatError):
    __error: Any
    _messageArgs: Any
    def __init__(self, error=None):
        ...
    def _getMessage(self):
        ...

class IncorrectCharacter(ChatError):
    def __init__(self):
        ...
    def _getMessage(self):
        ...

class AddFriendError(ChatError):
    __reason: Any
    _messageArgs: Any
    def __init__(self, reason):
        ...
    def _getMessage(self):
        ...

class AddIgnoredError(ChatError):
    __reason: Any
    _messageArgs: Any
    def __init__(self, reason):
        ...
    def _getMessage(self):
        ...

class SetMutedError(ChatError):
    __reason: Any
    _messageArgs: Any
    def __init__(self, reason):
        ...
    def _getMessage(self):
        ...

class UnsetMutedError(ChatError):
    __reason: Any
    _messageArgs: Any
    def __init__(self, reason):
        ...
    def _getMessage(self):
        ...

class UserIgnoredError(ChatError):
    __ignorerName: Any
    _messageArgs: Any
    def __init__(self, ignorerName):
        ...
    def _getMessage(self):
        ...

class CreatePrivateError(ChatError):
    __reason: Any
    _messageArgs: Any
    def __init__(self, reason):
        ...
    def _getMessage(self):
        ...

class ActiveChannelsLimitReached(ChatError):
    __limit: Any
    _messageArgs: Any
    def __init__(self, limit):
        ...
    def _getMessage(self):
        ...

class UsersRosterLimitReached(ChatError):
    __limit: Any
    _messageArgs: Any
    def __init__(self, limit):
        ...
    def _getMessage(self):
        ...

class ChatCommandError(ChatError):
    __error: Any
    _messageArgs: Any
    def __init__(self, response=None, error=None):
        ...
    def _getMessage(self):
        ...

class InviteCommandError(ChatError):
    __error: Any
    __inviteID: Any
    _messageArgs: Any
    def __init__(self, inviteID, response=None, error=None):
        ...
    def _getMessage(self):
        ...

class InviteCreateError(InviteCommandError):
    def __init__(self, response=None, error=None):
        ...

class InviteCreationNotAllowed(InviteCreateError):
    def __init__(self, response=None, error=None):
        ...

class ChatCommandInCooldown(ChatCommandError):
    _messageArgs: Any
    def __init__(self, command):
        ...

class ChatCommandNotAllowedError(ChatCommandError):
    def __init__(self):
        ...

class MemberAlreadyBanned(ChatCommandError):
    _messageArgs: Any
    def __init__(self, member):
        ...

class MemberAlreadyModerator(ChatCommandError):
    _messageArgs: Any
    def __init__(self, member):
        ...

class MemberNotModerator(ChatCommandError):
    _messageArgs: Any
    def __init__(self, member):
        ...

class IncorrectCommandArgumentError(ChatCommandError):
    _messageArgs: Any
    def __init__(self, arg):
        ...

class ChatException(ChatError):
    def __init__(self, response=None):
        ...

class ChannelNotExists(ChatException):
    __channelId: Any
    def __init__(self, id):
        ...
    def _getMessage(self):
        ...

class ChannelEntityUnreachable(ChatException):
    __channelId: Any
    def __init__(self, id):
        ...
    def _getMessage(self):
        ...

class UserNotExists(ChatException):
    __nickname: Any
    _messageArgs: Any
    def __init__(self, nickname):
        ...
    def _getMessage(self):
        ...

class MapRemovalReason(object):
    MAP_DISABLED = 1
    SLOT_DISABLED = 2

class MESSAGE_FILTER_TYPE(object):
    EXCLUDE = 1
    INCLUDE = 2

def __notifyFilterAll(originatorId, entityId):
    ...
def __notifyFilterNone(originatorId, entityId):
    ...
def __notifyFilterOnlyOriginator(originatorId, entityId):
    ...
def __notifyFilterExceptOriginator(originatorId, entityId):
    ...
def boundActionResponseFilter(response):
    ...
def buildChatActionData(action, channelId=None, **kwArgs):
    ...
def buildChannelsKey(id):
    ...
# decorador original: @noexcept
def getChannelsIDFromKey(key):
    ...
def isChannelSecured(channelInfo):
    ...
def _testChannelFlag(channelInfo, testedFlag, resultForNone=True):
    ...
def _testFlags(flags, testedFlag):
    ...
def isChannelDestroying(channelInfo):
    ...
def isChannelDestroyingFlags(flags):
    ...
def isPrivateChannel(channelInfo):
    ...
def isTrainingChannel(channelInfo):
    ...
def isPrebattleChannel(channelInfo):
    ...
def isPrebattleChannelFlags(flags):
    ...
def isSquadChannel(channelInfo):
    ...
def isTeamChannel(channelInfo):
    ...
def isBattleTeamFlags(flags):
    ...
def isArenaBattleTeamFlags(flags):
    ...
def isChannelHasVoice(channelInfo):
    ...
def isChannelHasVoiceFlags(flags):
    ...
def isClanChannel(channelInfo):
    ...
def isClanChannelFlags(flags):
    ...
def isTournamentChannelFlags(flags):
    ...
def isPrebattleClanChannelFlags(flags):
    ...
def isRegularChannel(channelInfo):
    ...
def isRegularChannelFlags(flags):
    ...
def initChatCooldownData():
    ...
def __isOperationInCooldown(cooldownDataInfo, operation, update=True):
    ...
def isOperationInCooldown(cooldownData, operation, update=True):
    ...
def getOperationCooldownPeriod(operation):
    ...
def isChatAdmin(username):
    ...
def __isCommandFromCategory(category, cmdName=None, cmdIdx=None):
    ...
def isInviteCommand(cmdName):
    ...
def isInviteCommandIdx(cmdIdx):
    ...
def isChannelChatCommand(cmdName):
    ...
def isChannelChatCommandIdx(cmdIdx):
    ...
def isUserCommand(cmdName):
    ...
def isUserCommandIdx(cmdIdx):
    ...
def isBattleChatCommand(cmdName):
    ...
def isBattleChatCommandIdx(cmdIdx):
    ...
def isSkipBanCheckForChatCommand(cmdName):
    ...
def isSkipBanCheckForCommandIdx(cmdIdx):
    ...
def isCommandMessage(message):
    ...
def parseCommandMessage(message, verifyArgs=True):
    ...
def verifyCommandData(command, int64Arg=0, int16arg=0, stringArg1='', stringArg2=''):
    ...
def isPermanentBan(banTime):
    ...
def isMembersListSupported(channelInfo):
    ...
def isMembersListSupportedByFlags(channelNotifyFlags):
    ...
def getMembersListMode(channelNotifyFlags):
    ...
def setMembersListMode(channelNotifyFlags, newMode):
    ...
def isFromFriendRoster(rosterData):
    ...
def isFromIgnoreRoster(rosterData):
    ...
def isVoiceMuted(rosterData):
    ...
def _checkRosterAccessBitmask(rosterData, bitmask):
    ...
def compressSysMessage(message):
    ...
def decompressSysMessage(message):
    ...
