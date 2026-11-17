# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/cooldown.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from chat_shared import isOperationInCooldown as isOperationInCooldown, CHAT_COMMANDS as CHAT_COMMANDS, getOperationCooldownPeriod as getOperationCooldownPeriod
import chat_shared as chat_shared
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from debug_utils import LOG_ERROR as LOG_ERROR
from helpers import i18n as i18n, html as html
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as I18N_INGAME_GUI
from messenger.formatters.users_messages import getBroadcastIsInCoolDownMessage as getBroadcastIsInCoolDownMessage
from messenger.m_constants import MESSENGER_I18N_FILE as MESSENGER_I18N_FILE
_battleChatShortcuts: tuple
_reloadingChatCommandsWithParams: tuple
_moderationChatCommands: tuple

def getBroadcastCoolDownMessage():
    ...
def isBroadcatInCooldown():
    ...
def isOperationInCooldownEx(operationName):
    ...
def getOperationCooldownPeriodEx(operationName):
    ...
def getBattleCommandExample(msgText):
    ...
def getOperationInCooldownMsg(operation, period, params=None):
    ...
