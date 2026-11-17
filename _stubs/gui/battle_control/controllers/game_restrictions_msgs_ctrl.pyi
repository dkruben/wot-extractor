# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/game_restrictions_msgs_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from constants import getTimeOnArena as getTimeOnArena, getArenaStartTime as getArenaStartTime
from messenger import MessengerEntry as MessengerEntry, g_settings as g_settings
from gui.battle_control.avatar_getter import getAvatarPlayLimits as getAvatarPlayLimits, getArenaUniqueID as getArenaUniqueID
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import time_utils as time_utils
_MAX_TIME = 2147483647

class GameRestrictionsMessagesController(Notifiable, IBattleController):
    TIME_RESERVE = 59
    THREE_MIN: Any
    TWO_MIN: Any
    ONE_MIN = time_utils.ONE_MINUTE
    CURFEW = 'curfew'
    DAILY = 'daily'
    WEEKLY = 'weekly'
    SESSION = 'session'
    __playLimits: Any
    __minutesCount: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def __getDailyPlayTimeLeft(self):
        ...
    def __getWeeklyPlayTimeLeft(self):
        ...
    def __getCurfew(self):
        ...
    def __getSessionPlayTimeLeft(self):
        ...
    def __getTimeLeft(self):
        ...
    def __getTimeLeftPriority(self):
        ...
    def __getNotificationStr(self):
        ...
    def __onBanNotifyHandler(self):
        ...
    def __getClosestSessionTimeNotification(self):
        ...

def createGameRestrictionsMessagesController():
    ...
