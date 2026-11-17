# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/denunciator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import constants as constants
from debug_utils import LOG_ERROR as LOG_ERROR
from helpers import dependency as dependency
from helpers import i18n as i18n
from gui import SystemMessages as SystemMessages
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from messenger import MessengerEntry as MessengerEntry, g_settings as g_settings
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, PlayerCtxStorage as PlayerCtxStorage
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
DENUNCIATIONS_MAP: dict

class DENUNCIATIONS(object):
    APPEAL = 'appeal'
    INCORRECT_BEHAVIOR = 'incorrectBehavior'
    NOT_FAIR_PLAY = 'notFairPlay'
    FORBIDDEN_NICK = 'forbiddenNick'
    BOT = 'bot'
    ORDER: tuple
    ENEMY_ORDER: tuple

class Denunciator(object):
    playerCtx: Any
    def makeAppeal(self, violatorID, userName, topic, arenaUniqueID):
        ...
    def isAppealsEnabled(self):
        ...
    def isAppealsForTopicEnabled(self, violatorID, topicID, arenaUniqueID):
        ...
    def getDenunciationsLeft(self):
        ...
    def _getViolatorKind(self, player, violatorID):
        ...
    def _makeNotification(self, message):
        ...

class LobbyDenunciator(Denunciator):
    itemsCache: Any
    def getDenunciationsLeft(self):
        ...
    def _getViolatorKind(self, player, violatorID):
        ...
    def _makeNotification(self, message):
        ...

class BattleDenunciator(Denunciator):
    sessionProvider: Any
    def getDenunciationsLeft(self):
        ...
    @classmethod
    def getArenaUniqueID(cls):
        ...
    def _getViolatorKind(self, player, violatorID):
        ...
    def _makeNotification(self, message):
        ...
